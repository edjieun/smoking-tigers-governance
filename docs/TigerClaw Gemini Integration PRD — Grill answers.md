1. On-Device Tier (OpenCode & Token Budgeting)

- **Fallback Behavior:** 
  
switch to a local model.  this is a user preference.  should be considered for setting up.
    
- **Code Privacy & Boundaries:** 
  
  we have a .gitignore and secrets.  we need to have governance rules and policies.  we have discussed in meetings, should be updated regularly.

2. On-Premises Tier (Orchestration & macOS Native Tools)

- **Tool Invocation Contract:** 

first, we need to build libraries.  native first.  then n8n workflow (or zapier or other service if available)
think of it as escalation tiers.  if it can't be resolved at the native script level.  escalate to n8n workflow.  if it requires an agent, a small model agent.  then escalate to gemini.  final escalation is the human in charge of the premise.  we don't want strict rules, that are rigid. building libraries and how local agents, subagents, are deployed is an ongoing WIP

    
- **Shared Script Library Schema:** 

libraries should be available to all repos on the device and use case.  want to avoid duplication.
Discovery is a local folder, that evolved.  there is still more to develop.


    
- **Human-in-the-Loop (HITL):** 

running silently is the objective.  permissions should be given ahead of time with our spec coding with openprojects methodology.