It sounds like you are ready to move beyond the consumer-facing chat interface and start building custom AI solutions. Since you are using a managed **Google Workspace** account (the `quorum.one` workspace), there are a few important things to understand about your access and the tools available to you.

### 1. Clarification on `deepmind.google`

It is important to note that [deepmind.google](https://deepmind.google/) is primarily an **informational and research website** showcasing Google’s AI breakthroughs. It is not a platform for building or hosting agents.

To build agents, you need to use Google’s developer-focused platforms: **Google AI Studio** or **Vertex AI**.

### 2. Your Path to Building Agents

Depending on your technical goals, you should choose between these two primary platforms:

#### Option A: Google AI Studio (Best for Prototyping)

If you want a fast, free, and intuitive way to experiment with Gemini, prompt engineering, and function calling (giving Gemini "tools" to perform actions), this is the place to start.

- **What it is:** A browser-based developer sandbox.
    
- **Best for:** Testing ideas, creating prototypes, and experimenting with "system instructions" and tools before committing to a larger project.
    
- **How to access it:** Go to [aistudio.google.com](https://aistudio.google.com/).
    
    - _Note:_ Because you are on a Workspace account, your administrator may need to explicitly enable "Google AI Studio" in the Google Admin Console. If you receive an error when signing in, you will need to ask your workspace admin to toggle this service on for your account.
        

#### Option B: Vertex AI (Best for Production & Enterprise)

If you are building an agent meant to be used by your team, clients, or integrated into your actual business workflows, use Vertex AI.

- **What it is:** Google Cloud’s enterprise-grade machine learning platform.
    
- **Best for:** Building secure, scalable, and compliant AI agents. It offers deep integration with your existing Google Cloud data, advanced monitoring, and "Agent Builder," which allows you to ground your agent in your own company's data (like documents or databases).
    
- **How to access it:** You will need access to the **Google Cloud Console**. This typically requires your organization to have a Google Cloud project set up with billing enabled.
    

### 3. How to Start Powering Agents with Skills and Tools

To give Gemini "skills" and "tools" (function calling), you will primarily work within the **System Instructions** and **Tools** sections of these platforms.

1. **Define the Agent's Purpose:** In AI Studio or Vertex AI, use the "System Instructions" area to define the persona and rules of your agent.
    
2. **Add Tools (Function Calling):** Both platforms allow you to define custom functions. You describe a tool (e.g., `get_weather`, `search_company_database`, or `send_email`) and its parameters. The Gemini model will then decide when to "call" that function, generate the necessary data, and pass it to your code to execute.
    
3. **Grounding:** If you want your agent to know facts about your company, use **Vertex AI Agent Builder** to connect the agent to your data stores (e.g., Google Drive, BigQuery, or public websites).
    

### Recommended Next Steps

1. **Check Access:** Try logging into [aistudio.google.com](https://aistudio.google.com/). If it works, start there—it is the lowest-friction way to learn how to use Gemini’s "tools" and "system instructions."
    
2. **Talk to your IT/Workspace Admin:** If you are blocked, send them a quick request: _"I am exploring Google's developer platforms (Google AI Studio/Vertex AI) for work-related projects. Could you please ensure these services are enabled for my account?"_
    
3. **Start with "System Instructions":** Once inside AI Studio, look at the **"System Instructions"** and **"Tools"** tabs on the right-hand side. This is where you actually define what the agent can "do" rather than just what it can "say."
---
Since you already have a GCP account, a Firebase website, and experience setting up service agents, you have all the necessary puzzle pieces. You just need to connect them.

Google has rolled out developer frameworks specifically designed to turn your Firebase and GCP infrastructure into full-fledged AI agents with custom tools and skills. Here is a roadmap of how to wire your stack together.

## 1. The Firebase Route: Give Your Website an Agent

Because you already have a Firebase setup, this is the fastest way to build an agent that uses tools and holds multi-turn conversations.

- **Use Firebase Genkit:** This is Google’s open-source framework designed explicitly for building full-stack, agentic apps. With Genkit, you can define an agent right in your code (TypeScript, Python, or Go), give it a system prompt, and attach custom JavaScript/Python functions as **Tools**.
    
- **How it works with your stack:** You can use Genkit's `Agents API` to deploy your agent as an HTTP endpoint (via Cloud Run or Cloud Functions). It natively integrates with **Firestore** to handle session states, chat history, and agent memory automatically.
    
- **Firebase AI Logic:** If you want your front-end Firebase website to communicate directly with Gemini models safely, use Firebase AI Logic. It handles client-side SDK calls, allows function calling (tools), and uses **Firebase App Check** to ensure unauthorized users can't hijack your API keys.
    

## 2. The GCP Route: Enterprise Tools & Service Agents

If your agent needs to perform backend workflows—like querying a private database, hitting internal APIs, or acting on behalf of a user—leverage your GCP infrastructure.

- **Gemini Enterprise Agent Platform (Formerly Vertex AI Agent Builder):** Google consolidated its enterprise AI tools under this platform.
    
- **Use the Agent Development Kit (ADK):** This is a code-first framework (Python, Go, Java, TypeScript) that allows you to build multi-turn agents. You can write custom code to orchestrate multiple sub-agents (e.g., an orchestrator agent that passes a task to a specialized database tool agent).
    
- **Leverage your Service Agents:** You can configure **Agent Gateways** inside GCP. This acts as a security layer, allowing the Gemini model to trigger tool executions safely while inheriting the exact IAM permissions and service account roles you define in GCP.
    

## 3. The Private & On-Device AI Route

Since you are experimenting with private and on-device AI, Google provides two distinct pathways depending on your architecture:

### A. True On-Device AI (No Cloud Latency/Costs)

If you want the AI logic to execute natively on a user's machine or phone inside your app without calling Google’s servers:

- **Google AI Edge & LiteRT-LM:** Google AI Edge provides a runtime called **LiteRT-LM** (built on the evolution of TensorFlow Lite). It allows you to run smaller, open-weights models locally across Android, iOS, or Web browsers.
    
- **Gemini Nano:** For mobile-specific features, you can interface with **Gemini Nano** via Android's AICore system service to handle client-side summarization, rewriting, or light reasoning without leaving the device.
    

### B. Private Cloud AI (Enterprise Data Privacy)

If you want the power of a large model like Gemini 1.5 Pro but need complete data privacy:

- Use the **Gemini Enterprise Agent Platform** alongside **Model Armor**. This ensures that data passed to your agent tools is scanned for threats, filtered, and completely isolated within your GCP project boundary. None of the data is used to train Google’s base models.
    
- Alternatively, you can pull open-source weights (like the **Gemma** family) from the Model Garden and host them yourself on a private Google Kubernetes Engine (GKE) cluster or custom Vertex endpoint.
    

## Your Concrete Next Steps

1. **Fire up the Genkit Developer UI:** Run `npm init genkit` or the Python equivalent locally in a terminal. It spins up a brilliant local developer UI where you can visually write prompts, define tools, and trace exactly how the model decides to use them before deploying anything to Firebase.
    
2. **Build a "Hello World" Tool:** In Genkit or AI Studio, write a simple function (e.g., a function that fetches the current time or a random item from a JSON array) and pass it to the model as a tool. Ask the model a question that requires that data and watch it switch from "chatting" to "tool execution."
    
3. **Map out your Cloud architecture:** Decide if your Firebase site needs to just talk to the model (Genkit), or if you need robust, secure multi-agent workflows that connect directly to your broader GCP databases (Gemini Enterprise Platform).
---

Ditching the "OpenRouter tax" makes total sense, especially when you already have access to Google's ecosystem. Google AI Studio offers an incredibly generous free tier, giving you massive token limits for models like Gemini Flash and Pro without costing a dime for development and prototyping.

You can completely replace OpenRouter and Claude Sonnet in your current stack with Gemini, keeping your VS Code setup, GitHub workflows, and OpenProject integrations intact—all for $0.

## 1. Swap OpenRouter for Gemini in VS Code

To stop paying OpenRouter for your IDE autocomplete and chat, you just need to switch the backend extension in VS Code to use a free Google AI Studio API key.

- **The Tool:** Install the **Continue** extension (continue.dev) or **Cline / Roo Code** in VS Code. These are open-source AI coding assistants that let you bring your own API keys.
    
- **The Key:** Go to your Google AI Studio dashboard, click **Create API Key**, and generate a key.
    
- **The Setup:** In the extension settings (usually a `config.json` or `config.yaml` file), set your provider to `gemini` and paste your AI Studio API key. You can use **Gemini Pro** for heavy reasoning and coding tasks, and **Gemini Flash** for lightning-fast autocomplete.
    

## 2. Re-wire Your Custom Agents for Free

If you were using OpenRouter to power external agents or tools that interact with OpenProject or GitHub, you can route them directly through the native Gemini API.

Instead of paying per token via OpenRouter, use your free AI Studio key directly in your agent code:

- **If using Python/TypeScript:** Use the official `@google/genai` SDK. You simply swap the OpenRouter base URL/client initialization for the Google GenAI client.
    
- **For Agentic Workflows:** If you want your agent to interact with **OpenProject** (e.g., reading tickets, updating tasks) or **GitHub** (e.g., reviewing PRs), you can use Gemini’s native **Function Calling (Tools)**. You write the code to talk to the OpenProject/GitHub APIs, declare those functions to Gemini, and the model will autonomously execute them using your free API key.
    

## 3. How the New Stack Looks

|**Component**|**Old Way (Paid)**|**New Way (Free)**|
|---|---|---|
|**IDE AI / Chat**|VS Code + OpenRouter (Sonnet)|VS Code + Continue / Cline (**Gemini Pro**)|
|**Code Autocomplete**|OpenRouter (Sonnet)|Continue / Cline (**Gemini Flash**)|
|**Agent Backbone**|OpenRouter API calls|Native **Google AI Studio API** (Free Tier)|
|**Project & Code Management**|OpenProject & GitHub|OpenProject & GitHub (Unchanged)|

## Next Steps to Cut the Cost

1. Go to [aistudio.google.com](https://aistudio.google.com/) and grab a fresh API key.
    
2. Open VS Code, install **Continue**, and paste the key into the configuration.
    
3. Point your custom service agents/scripts away from OpenRouter endpoints and directly to the Google Gemini API using your new key.
    

This workflow walks through setting up the free Google AI Studio API key directly inside VS Code using the Continue extension to eliminate code assistant fees completely.

---
Thanks for clarifying! Knowing that you are using **GitHub Copilot's new native BYOK (Bring Your Own Key)** mode and have **OpenCode** installed changes the playbook completely.

You can completely bypass OpenRouter (and its pay-per-token model) by routing both Copilot and OpenCode directly through **Google AI Studio's generous free tier**.

Here is exactly how to reconfigure both tools to use Gemini for free.

## Part 1: Swap OpenRouter for Gemini in GitHub Copilot Chat

GitHub Copilot’s Custom Endpoint feature allows you to use any OpenAI-compatible endpoint. Google AI Studio provides exactly that format for free.

### Step 1: Get Your Free Google Key

1. Go to [aistudio.google.com](https://aistudio.google.com/) and create a free API key.
    

### Step 2: Update VS Code's Language Models

1. Open the Command Palette (`Cmd+Shift+P` on Mac / `Ctrl+Shift+P` on Windows/Linux).
    
2. Search for and select **Chat: Manage Language Models**.
    
3. Click **+ Add Models** and select **Custom Endpoint**.
    
4. Name the group something clear (e.g., `Google Free Tier`).
    
5. Paste your free Google AI Studio API key when prompted.
    
6. Choose **Chat Completions API** as the API type.
    

### Step 3: Configure `chatLanguageModels.json`

VS Code will automatically open your hidden `chatLanguageModels.json` configuration file. Update the `models` array inside your new Google block to look like this:

JSON

```
{
  "name": "Google Free Tier",
  "vendor": "customendpoint",
  "apiKey": "${input:chat.lm.secret.your-generated-id}", 
  "apiType": "chat-completions",
  "models": [
    {
      "id": "gemini-2.5-flash",
      "name": "Gemini Flash (Free)",
      "url": "https://generativelanguage.googleapis.com/v1beta/openai",
      "toolCalling": true,
      "vision": true,
      "maxInputTokens": 1048576
    },
    {
      "id": "gemini-2.5-pro",
      "name": "Gemini Pro (Free)",
      "url": "https://generativelanguage.googleapis.com/v1beta/openai",
      "toolCalling": true,
      "vision": true,
      "maxInputTokens": 2097152
    }
  ]
}
```

> ⚠️ **Crucial Gotchas:**
> 
> - **Do not hardcode your API key** directly into this JSON file. Leave the `${input:chat.lm.secret...}` string intact that VS Code auto-generated.
>     
> - Keep `"vendor": "customendpoint"` exactly as is, otherwise VS Code won't render it in the picker.
>     
> - Note the `url`: **Do not add `/chat/completions` to the end of the URL.** VS Code appends that automatically behind the scenes.
>     

Save the file, reload VS Code, and you can now select **Gemini Pro** or **Flash** right inside your regular Copilot Chat and Agent dropdowns—completely free.

## Part 2: Swap OpenRouter for Gemini in OpenCode

OpenCode is an open-source terminal coding agent that natively supports Google Gemini without needing OpenRouter proxies.

### Option A: Via the OpenCode UI Sidebar

If you use the OpenCode VS Code extension interface:

1. Open the OpenCode sidebar tab.
    
2. Click the **Agent/Model Dropdown** at the top of the chat panel.
    
3. Instead of selecting OpenRouter, look for the native **Google Gemini** provider section.
    
4. Paste your AI Studio API key and choose `gemini-2.5-pro` or `gemini-2.5-flash`.
    

### Option B: Via the Terminal (CLI)

If you run OpenCode straight from your VS Code integrated terminal:

Simply export your Google API key to your environment before running the agent:

Bash

```
export GEMINI_API_KEY="your_free_ai_studio_key"
opencode
```

OpenCode will detect the environment variable automatically, bypass OpenRouter entirely, and allow you to select Gemini models directly for execution.

### Your New Setup Summary

- **GitHub Copilot Chat & Agent Mode:** Uses VS Code BYOK via the Google OpenAI-compatible endpoint (Free).
    
- **OpenCode Agent Execution:** Uses native Google Gemini provider configurations (Free).
    
- **OpenRouter / Anthropic Cost:** **$0.**
    

Give the Custom Endpoint configuration a try in VS Code. Let me know if you run into any parsing errors when editing the JSON layout!

---

Google AI Studio’s free tier is one of the most developer-friendly sandboxes available, but because you are operating inside a managed workspace (`quorum.one`) and planning to wire up agents, you need to look closely at the fine print.

## 1. The Precise Quotas & Rate Limits

Google measures your free tier usage across three separate dimensions: **Requests Per Minute (RPM)**, **Tokens Per Minute (TPM)**, and **Requests Per Day (RPD)**. Limits are calculated **per project**, meaning if you have three different VS Code extensions or custom agents sharing the same project API key, they all pull from the same pool.

Quotas vary drastically depending on the model tier you target:

### Gemini Flash Models (e.g., Gemini 2.5 / 3.5 Flash)

_Optimized for fast autocomplete, routing, and lightweight agent tasks._

- **RPM:** ~10 to 15 requests per minute
    
- **TPM:** ~1 Million tokens per minute
    
- **RPD:** ~250 to 1,500 requests per day
    

### Gemini Pro Models (e.g., Gemini 2.5 / 3.1 Pro)

_Optimized for deep coding, complex reasoning, and agent orchestrators._

- **RPM:** ~2 to 5 requests per minute
    
- **TPM:** ~32,000 tokens per minute
    
- **RPD:** ~100 requests per day
    

_Note: Daily quotas (RPD) reset at midnight Pacific Time._

## 2. The Hard Restrictions

Before building anything substantial, there are two massive architectural restrictions you must account for on the Free Tier:

- **Data Privacy (The Catch):** On the Free Tier, **your prompt inputs and model outputs are used by Google to train and improve its products.** Human reviewers may also read obfuscated snippets. Because you belong to an organization workspace (`quorum.one`), **do not** feed corporate data, proprietary customer records, or highly confidential code into the free tier.
    
    - _The Fix:_ As soon as you switch your AI Studio project to the **Paid Tier (Pay-As-You-Go)**, your data is completely isolated, and Google is legally restricted from using it for training.
        
- **Production Constraints:** Because of the tight RPM and RPD limits, you cannot use the free tier to host an agent that multiple people in your company will use simultaneously. It will immediately throw `429 Rate Limit Exceeded` errors.
    

## 3. Do You Need to Track Tokens?

### Financially? No.

You do not need to track tokens for budgeting purposes. Google AI Studio's free tier requires no credit card links or billing parameters. If you hit a limit, the API simply pauses and drops a 429 error until your minute or day resets. You will never receive a surprise bill.

### Operationally? Yes, Absolutely.

While you don't have to watch your wallet, you **must** track your token usage programmatically for two reasons:

1. **The Context Window Trap:** Gemini models boast massive context windows (1 to 2 million tokens). It is tempting to dump your entire codebase or a massive database into the context. However, if you upload a 500,000-token project context on the free tier, you will exhaust your total daily token allowance or trigger a TPM block in just a couple of prompts.
    
2. **Agent Logic Loops:** When agents execute "tools" (function calling), they often make multiple background calls to the LLM in a single minute to figure out the right parameters. An agent workflow can easily eat up 10 requests in 15 seconds, maxing out your Free tier RPM instantly.
    

### The Verdict for Your Stack

Keep your VS Code extensions (like GitHub Copilot custom endpoints or OpenCode) on the **Free Tier** for personal engineering and prompt drafting—just don't pass them company secrets.

If you decide to deploy your Firebase agent site for the rest of your team to use, you will want to link a GCP billing account to your project. Upgrading to "Tier 1" paid usage removes the data training restriction and drops token costs down to fractions of a cent (e.g., ~$0.30 to $0.75 per million tokens on Flash models), which is still vastly cheaper than paying OpenRouter premiums.

---
