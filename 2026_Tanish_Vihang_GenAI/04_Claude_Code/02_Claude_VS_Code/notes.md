# MCP Servers

### Context7 mcp server

install command to run it locally (via npx):
`claude mcp add context7 -- npx -y @upstash/context7-mcp`


install command to run it as a remote MCP server (no need to install node.js or npm):
`claude mcp add --transport http context7 https://mcp.context7.com/mcp`

### Configuration Scopes
- User: Applies to all your projects, kind of global for your user. Files that hold this setting: `~/.claude/settings.json`, `~/.claude.json`
- Project: Tied to a particular project only. Shared with the team via git commit. Files that hold this setting: `.mcp.json`, `.claude/settings.json`
- Local: "User + Project". Means, tied to that computer only (git-ignored: doesn't get pushed on to the git) AND also tied to this project only (not shared with other folders). Files that hold this setting: `.claude/settings.local.json`, `~/.claude.json`

**Conflict Resolution: Narrowest scope (local) always wins**

Order of precidence: **`Local > Project > User`**