title is a reference to this https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/246/activity

# task description
There needs to be a template for task description.  
  
"Post test transcript to #transcripts; verify #tasks + #decisions populate", this should be here

from context and intent, it's about meeting notes.  i don't know in which app, what process.  verifying tasks plus decisions means changes to OP.  updating meeting, attaching files, relationships, tasks.  that summary should include a link back to here.  
  
Regardless if we are talking about adding to mattermost, which I assume this is about.  or using the Nerve dashboard, or Discord, or being fully automated with meeting that we schedule  
  

Instead of being written in description.  People assigned should be below.  I am the only person in here right now.  members must have a <user>@quourm.one address
  
# People
when adding a user to a project assign their role and draft an message. this is sent to multiple communications channels email, discord, mm, slack, telegram, whatsapp, depending on user preference.

 invitation should have a message
 
OpenProject's "People" management features ==allow you to build, track, and organize project teams across your organization==. You can assign specific roles and permissions to internal staff and external partners, track cross-functional workloads, and manage company-wide team member profiles. [[1](https://www.openproject.org/de/blog/the-perfect-project-team/), [2](https://www.openproject.org/blog/the-perfect-project-team/)]

Managing Project Teams

- **Add Members:** Navigate to your project, select **Members** from the left-hand menu, and click **+ Member** to invite users or user groups to a specific project. [[1](https://www.openproject.org/docs/user-guide/members/)]

- **Define Roles:** Assign custom permission sets (e.g., Project Manager, Viewer, or Member) to control who can view, edit, or delete work packages. [[1](https://www.openproject.org/docs/project-management-guide/4-project-organisation-and-roles/), [2](https://www.openproject.org/okr-software/), [3](https://www.openproject.org/pmflex/), [4](https://massivegrid.com/blog/xwiki-openproject-wiki-project-management/), [5](https://www.openproject.org/blog/the-perfect-project-team/)]

- **External Collaboration:** Invite external stakeholders, clients, or vendors directly to projects and optimize costs by adjusting their access levels. [[1](https://www.openproject.org/blog/the-perfect-project-team/), [2](https://www.openproject.org/de/blog/the-perfect-project-team/)]

# Device

Mac Mini (Scout / OpenClaw :18789)  
AI Agents working on our behalf should be able identified
 harness, model, contxt, agent.md, skills.md, tools, hardware location, port mapping.
  
# Blocks
: all Phase 4
OpenProject ==primarily uses "Blocks" and "Blocked by" relations to track task dependencies and project bottlenecks==. This ensures team members can easily identify which tasks are preventing others from progressing.

In OpenProject, you can define dependency restrictions between work packages so that if one task is blocked, the downstream tasks are paused or flagged. [[1](https://www.openproject.org/docs/user-guide/work-packages/work-package-relations-hierarchies/)]

- **Set a Blocked Relation:** Open a work package, navigate to the **Relations** tab, and select **Blocks** or **Blocked by**.

- **Visualizing Dependencies:** Use the native Gantt chart or Work Package tables to see which issues are causing project bottlenecks at a glance. You can track dependencies directly using the [OpenProject Work Package Relations Documentation](https://www.openproject.org/docs/user-guide/work-packages/work-package-relations-hierarchies/). [[1](https://www.openproject.org/docs/user-guide/work-packages/work-package-relations-hierarchies/), [2](https://www.openproject.org/blog/how-to-work-with-work-packages/), [3](https://www.openproject.org/docs/use-cases/okr-management/), [4](https://www.openproject.org/docs/user-guide/work-packages/work-package-relations-hierarchies/)]
  
# Deadline: next session
add due dates

# estimates and progress
OpenProject ==tracks task estimates and progress under the **Estimates and Progress** section of work packages==. It utilizes two main attributes: **Work** (total estimated hours/days) and **Remaining work**. Progress is calculated using one of two automatic reporting modes: [[1](https://www.openproject.org/docs/user-guide/time-and-costs/progress-tracking/), [2](https://www.openproject.org/blog/openproject-14-0-release/), [3](https://www.openproject.org/collaboration-software-features/time-tracking/)]

- **Work-based reporting:** The % Complete is calculated automatically based on the ratio of _Work_ to _Remaining work_.

- **Status-based reporting:** The % Complete is fixed and automatically updates based on the current status (e.g., "New" is 0%, "In Progress" is 50%, and "Closed" is 100%). [[1](https://www.openproject.org/blog/changes-progress-work-estimates/), [2](https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-progress-tracking/), [3](https://www.openproject.org/docs/user-guide/time-and-costs/progress-tracking/)]

For higher-level tracking, OpenProject automatically rolls up these figures to parent tasks and phases. This aggregation can be calculated using a simple average or weighted by the _Work_ hours. [[1](https://www.openproject.org/docs/user-guide/work-packages/work-packages-faq/), [2](https://www.openproject.org/pt/blog/changes-progress-work-estimates/), [3](https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-progress-tracking/)]

You can configure these settings and read more about the system behaviors directly on the [OpenProject Progress Tracking Guide](https://www.openproject.org/docs/user-guide/time-and-costs/progress-tracking/).

# attach files
add links to google docs

# relations
In OpenProject, work package **relations** ==connect tasks to establish dependencies, hierarchies, and chronological sequences==. They help track how work is intertwined, and some conditional relations can automatically adjust task start and end dates in your scheduling views

# meetings
https://www.openproject.org/docs/user-guide/meetings/


