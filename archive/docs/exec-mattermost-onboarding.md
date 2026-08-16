# Mattermost Access — Executive Council Onboarding

**Status:** Draft v1.0 · **Owner:** Ed Hwang (Steward)

---

## What This Is

Smoking Tigers runs a private Mattermost server for executive coordination and interaction with Scout (our AI Chief of Staff). We use Mattermost + Tailscale instead of Slack or Discord because:

- **It's fully private.** The server runs on Ed's home machine and is only accessible through our encrypted private network — nothing is exposed to the public internet.
- **We own our data.** No third-party platform has access to our conversations.
- **Scout lives here.** This is the primary channel for working with Scout.

To connect, you'll install two free apps: **Tailscale** (private network access) and **Mattermost** (the chat app). The whole process takes about 5 minutes.

---

## What You Need

| Item | What It Does | Cost |
|------|-------------|------|
| **Tailscale** | Connects your device to our private network | Free |
| **Mattermost** | The chat app (like Slack) | Free |
| **Network invite** | Ed will send you a Tailscale invite link | — |
| **Login credentials** | Ed will create your Mattermost account | — |

---

## Step 1: Install Tailscale

Download and install Tailscale on any device you want to use:

- **macOS:** [Mac App Store](https://apps.apple.com/app/tailscale/id1475387142)
- **iOS:** [App Store](https://apps.apple.com/app/tailscale/id1470499037)
- **Android:** [Google Play](https://play.google.com/store/apps/details?id=com.tailscale.ipn)
- **Windows:** [tailscale.com/download/windows](https://tailscale.com/download/windows)

After installing:

1. Open Tailscale.
2. Click the invite link Ed sends you.
3. Sign in when prompted — this joins you to our private network.
4. Make sure Tailscale shows **Connected** (you'll see a small icon in your menu/task bar).

> 💡 Tailscale needs to stay connected whenever you want to use Mattermost. Think of it like a VPN toggle.

---

## Step 2: Install Mattermost

Download the Mattermost app:

**Desktop:**
- **macOS / Windows / Linux:** [mattermost.com/apps](https://mattermost.com/apps/)

**Mobile:**
- **iOS:** [App Store](https://apps.apple.com/app/mattermost/id1257222717)
- **Android:** [Google Play](https://play.google.com/store/apps/details?id=com.mattermost.rn)

---

## Step 3: Connect to Mattermost

1. Open the Mattermost app.
2. Tap **Add Server** (or enter the server URL when prompted).
3. Enter the server address:

   ```
   http://edlicious-server:8065
   ```

4. Log in with the username and password Ed provides.

That's it — you should see the Smoking Tigers workspace.

---

## Step 4: Verify

Once you're in, post a message in the **#executive** channel to confirm you're connected. A simple "I'm here 👋" works great.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| **Can't reach the server** | Make sure Tailscale is connected (check the icon in your menu bar). |
| **Still can't connect** | Try the IP address instead: `http://100.122.103.40:8065` |
| **Forgot your password** | Ask Ed or Scout to reset it. |
| **Tailscale says "not connected"** | Open the Tailscale app and toggle it on. |
| **App asks for a server URL** | Enter `http://edlicious-server:8065` |

If something else comes up, message Ed directly — he'll sort it out.

---

## Security Notes

- **Your connection is encrypted.** Tailscale creates a private, encrypted tunnel between your device and the server.
- **Nothing is on the public internet.** The Mattermost server is only reachable through our Tailscale network.
- **Do not share** your Tailscale invite link or Mattermost credentials with anyone outside the executive council.
- **HTTP is fine here.** Since we're on a private encrypted network, you don't need HTTPS — the Tailscale tunnel handles security.

---

*Questions? Reach out to Ed or Scout.*
