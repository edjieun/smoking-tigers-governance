#!/usr/bin/env bash
# setup-secrets.sh
# Phase 0: Secrets management setup.
#
# Vault format: vault.tar.gz.enc — a tar.gz of .env + google/ credentials,
# encrypted with AES-256-CBC using a passphrase stored at ~/.ste-secrets/.passphrase.
# The passphrase file is NEVER committed. It lives in Apple Passwords and on-disk (chmod 600).
#
# Restore on any rebuild:
#   git clone https://github.com/edjieun/ste-secrets.git ~/ste-secrets-repo
#   openssl enc -d -aes-256-cbc -pbkdf2 \
#     -pass file:~/.ste-secrets/.passphrase \
#     -in ~/ste-secrets-repo/vault.tar.gz.enc | tar xzf - -C ~/.ste-secrets
#   source ~/.ste-secrets/.env
#
# Usage:
#   bash scripts/setup-secrets.sh [init|encrypt|decrypt|check]
#
#   init     — create a new .env template; you fill in the values
#   encrypt  — encrypt .env + google/ → vault.tar.gz.enc (non-interactive, uses ~/.ste-secrets/.passphrase)
#   decrypt  — decrypt vault.tar.gz.enc → ~/.ste-secrets/.env + google/ (non-interactive)
#   check    — verify all required secrets are present in current .env

set -euo pipefail

SECRETS_DIR="$HOME/.ste-secrets"
ENV_FILE="$SECRETS_DIR/.env"
ENV_ENC_FILE="$SECRETS_DIR/.env.enc"
VAULT_FILE="$HOME/ste-secrets-repo/vault.tar.gz.enc"
PASSPHRASE_FILE="$SECRETS_DIR/.passphrase"

# ── Required secrets ──────────────────────────────────────────────────────
REQUIRED_KEYS=(
  OPENROUTER_API_KEY
  GITHUB_TOKEN
  MATTERMOST_URL
  MATTERMOST_TOKEN
  MATTERMOST_TEAM
  TAILSCALE_AUTH_KEY
  LMSTUDIO_API_BASE
  OPENPROJECTS_URL
  OPENPROJECTS_API_KEY
)

CMD="${1:-check}"

case "$CMD" in

  init)
    mkdir -p "$SECRETS_DIR"
    if [[ -f "$ENV_FILE" ]]; then
      echo "⚠️  $ENV_FILE already exists. Delete it first if you want to reinitialize."
      exit 1
    fi

    cat > "$ENV_FILE" << 'EOF'
# STE On-Premise AI — Secrets
# Fill in each value, then run: bash scripts/setup-secrets.sh encrypt

# OpenRouter (cloud model fallback — LAPTOP ONLY, not Mac Mini)
OPENROUTER_API_KEY=

# GitHub (governance repo, agents repo, secrets repo)
GITHUB_TOKEN=

# Mattermost (OpenClaw comms — Mac Mini)
MATTERMOST_URL=https://your-mattermost-instance.com
MATTERMOST_TOKEN=
MATTERMOST_TEAM=smoking-tigers

# Tailscale (private network auth)
TAILSCALE_AUTH_KEY=

# LM Studio server (Mac Mini inference endpoint — used by laptop OpenCode)
# Format: http://<macmini-tailscale-ip>:1234/v1
LMSTUDIO_API_BASE=http://100.x.x.x:1234/v1

# OpenProjects (M1 MacBook — transparency/orchestration layer)
OPENPROJECTS_URL=http://100.x.x.x:8080
OPENPROJECTS_API_KEY=
EOF

    chmod 600 "$ENV_FILE"
    echo "✅ Template created at: $ENV_FILE"
    echo ""
    echo "Next steps:"
    echo "  1. Edit $ENV_FILE and fill in all values"
    echo "  2. Run: bash scripts/setup-secrets.sh encrypt"
    echo "  3. Commit .env.enc to your private GitHub repo"
    echo "  4. NEVER commit the unencrypted .env file"
    ;;

  encrypt)
    if [[ ! -f "$ENV_FILE" ]]; then
      echo "Error: $ENV_FILE not found. Run 'init' first."
      exit 1
    fi
    if [[ ! -f "$PASSPHRASE_FILE" ]]; then
      echo "Error: Passphrase file not found at $PASSPHRASE_FILE"
      echo "Copy it from Apple Passwords or another machine (chmod 600)."
      exit 1
    fi
    if [[ ! -d "$(dirname "$VAULT_FILE")" ]]; then
      echo "Error: ste-secrets-repo not found at ~/ste-secrets-repo"
      echo "Clone it first: git clone https://github.com/edjieun/ste-secrets.git ~/ste-secrets-repo"
      exit 1
    fi

    echo "Encrypting vault → $VAULT_FILE"
    cd "$SECRETS_DIR"
    tar czf - .env google/ | openssl enc -aes-256-cbc -pbkdf2 \
      -pass file:"$PASSPHRASE_FILE" \
      -out "$VAULT_FILE"
    echo ""
    echo "✅ Encrypted: $VAULT_FILE"
    echo ""
    echo "Next steps:"
    echo "  cd ~/ste-secrets-repo && git add vault.tar.gz.enc && git commit -m 'update vault' && git push"
    ;;

  decrypt)
    if [[ ! -f "$VAULT_FILE" ]]; then
      echo "Error: vault not found at $VAULT_FILE"
      echo "Clone the secrets repo first:"
      echo "  git clone https://github.com/edjieun/ste-secrets.git ~/ste-secrets-repo"
      exit 1
    fi
    if [[ ! -f "$PASSPHRASE_FILE" ]]; then
      echo "Error: Passphrase file not found at $PASSPHRASE_FILE"
      echo "Copy it from Apple Passwords or another machine:"
      echo "  ssh <other-machine> 'cat ~/.ste-secrets/.passphrase' > $PASSPHRASE_FILE && chmod 600 $PASSPHRASE_FILE"
      exit 1
    fi

    mkdir -p "$SECRETS_DIR"
    echo "Decrypting vault → $SECRETS_DIR"
    openssl enc -d -aes-256-cbc -pbkdf2 \
      -pass file:"$PASSPHRASE_FILE" \
      -in "$VAULT_FILE" | tar xzf - -C "$SECRETS_DIR"
    chmod 600 "$ENV_FILE"
    chmod 600 "$SECRETS_DIR"/google/*.json 2>/dev/null || true
    echo ""
    echo "✅ Decrypted to: $SECRETS_DIR"
    echo ""
    echo "To load secrets into your current shell:"
    echo "  source $ENV_FILE"
    echo ""
    echo "To load automatically on shell startup, add to ~/.zshrc:"
    echo "  [ -f $ENV_FILE ] && source $ENV_FILE"
    ;;

  check)
    if [[ ! -f "$ENV_FILE" ]]; then
      echo "⚠️  No .env found at $ENV_FILE"
      echo "Run 'init' to create a template or 'decrypt' to restore from encrypted backup."
      exit 1
    fi

    # shellcheck source=/dev/null
    source "$ENV_FILE"

    echo "Checking required secrets..."
    echo ""
    MISSING=0
    for key in "${REQUIRED_KEYS[@]}"; do
      val="${!key:-}"
      if [[ -z "$val" ]]; then
        echo "  ❌ MISSING: $key"
        MISSING=$((MISSING + 1))
      else
        # Show first 4 chars only
        masked="${val:0:4}****"
        echo "  ✅ $key = $masked"
      fi
    done

    echo ""
    if (( MISSING > 0 )); then
      echo "⚠️  $MISSING secret(s) missing. Edit $ENV_FILE and fill them in."
      exit 1
    else
      echo "✅ All secrets present."
    fi
    ;;

  *)
    echo "Usage: bash scripts/setup-secrets.sh [init|encrypt|decrypt|check]"
    exit 1
    ;;
esac
