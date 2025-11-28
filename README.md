# Hi, I'm Daniel 👋

## Building offline-first developer tools

I ship production-ready infrastructure that solves real problems for developers.

**Currently:** Launching [SyncKit](https://github.com/Dancode-188/synckit) - an offline-first sync engine ([npm](https://www.npmjs.com/package/@synckit-js/sdk))

**Previously:**
- [Graft](https://github.com/Dancode-188/graft) - Keyboard-first Git GUI (free alternative to $99+ tools)
- [RestBolt](https://github.com/Dancode-188/restbolt) - Fast, local-first API testing tool

**Focus:** Distributed Systems, CRDTs, Offline-First Architecture, Developer Experience

**Location:** Nairobi, Kenya 🇰🇪

---

## 🚀 Featured Projects

### **SyncKit** - Offline-First Sync Engine

**The problem I solved:** After building RestBolt and Graft, I kept hitting the same wall - adding cross-device sync meant months of infrastructure work. Firebase isn't truly offline-first, Supabase has no offline support, Automerge/Yjs have steep learning curves.

**What I built:** Production-ready sync infrastructure that developers can drop into local-first apps in minutes, not months.

**Impact:**
- 232+ GitHub stars in first 24 hours (well above average for HN launches)
- Published to npm with production-ready v0.1.0
- Formal TLA+ verification caught 3 critical bugs before writing any code
- 700+ tests including 80 chaos tests - zero data loss
- 59KB bundle (smaller than most icon libraries)

**Why it matters:** I built the infrastructure I wish existed - bridging the gap between "too complex" and "too restrictive" so developers can focus on their products, not sync logic.

**Tech Stack:** Rust, WebAssembly, TypeScript, TLA+, PostgreSQL, Redis, Docker

![npm version](https://img.shields.io/npm/v/@synckit-js/sdk) ![npm downloads](https://img.shields.io/npm/dt/@synckit-js/sdk) ![License](https://img.shields.io/badge/license-MIT-blue)

**Links:** [GitHub](https://github.com/Dancode-188/synckit) • [npm](https://www.npmjs.com/package/@synckit-js/sdk) • [Documentation](https://github.com/Dancode-188/synckit#readme)

---

### **Graft** - Keyboard-First Git GUI

**The problem:** Git GUIs are either expensive ($99/year), mouse-heavy and slow, or missing power features. Developers deserve better.

**What I built:** A production-ready Git GUI with native performance (Tauri + Rust), command palette (Cmd+K), and full Git power—completely free and open source.

**Key features:**
- ⚡ Keyboard-first design - Command palette, quick search, 20+ shortcuts
- 🎯 Power user features - Interactive rebase, stash management, visual branch graph
- 🚀 Native performance - <1s startup, handles 10,000+ commits smoothly
- 🎨 Beautiful themes - Professional dark/light themes with WCAG AA accessibility
- 💰 Free alternative - Does what GitKraken ($99/yr), Tower ($99), and Sublime Merge ($99) do

**Why it matters:** Most developers either pay $99+ for GitKraken/Tower or settle for limited free options. Graft delivers professional features with a keyboard-first workflow—for free.

**Tech Stack:** Tauri, Rust, React, TypeScript, Git (libgit2)

![GitHub stars](https://img.shields.io/github/stars/Dancode-188/graft?style=social) ![Version](https://img.shields.io/badge/version-1.0.3-green) ![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)

[View Project →](https://github.com/Dancode-188/graft)

---

### **RestBolt** - Fast, Local-First API Client

**The problem:** Existing API clients like Postman and Insomnia are slow (seconds to launch), memory-hungry (100s of MB), and force cloud-first workflows with constant sign-in prompts.

**What I built:** A from-scratch API testing tool built for speed and developer experience. Launches instantly, runs 100% offline, and respects local-first workflows.

**Key innovation - Chain Builder:**
Visual workflow editor for multi-step API testing. Extract variables from responses using JSONPath, automatically pipe data between requests, and execute complex workflows with proper error handling. Turns tedious manual testing (auth → create resource → verify → cleanup) into automated pipelines.

**Architecture decisions:**
- **Local-first storage:** Dexie.js (IndexedDB) for offline-capable persistence
- **Professional editor:** Monaco (VS Code's editor) for request/response viewing
- **Zero cloud dependencies:** Everything works offline, no forced sync
- **Type-safe:** Full TypeScript with Zustand state management

**Impact:**
- Production-ready features: Collections, environments, history, code generation (cURL, JS, Python)
- Keyboard-first UX with professional shortcuts (Cmd+Enter to send, etc.)
- Full HTTP method suite with WebSocket support
- Growing contributor base with active PRs and discussions

**Why it matters:** Proved you can build a professional-grade developer tool without cloud bloat, forced accounts, or sacrificing features. Fast, local, powerful.

**Tech Stack:** Next.js 15, TypeScript, Zustand, Dexie.js, Monaco Editor, Tailwind CSS

[View Project →](https://github.com/Dancode-188/restbolt)

---

## 🛠️ Technology Stack

**Core:** Rust, TypeScript, JavaScript, Python  
**Frontend:** React, Next.js, Electron, Tauri, Tailwind CSS  
**Backend:** Node.js, Bun, Hono, FastAPI  
**Distributed Systems:** CRDTs, TLA+, WebAssembly  
**Databases:** PostgreSQL, Redis, MongoDB, IndexedDB  
**Infrastructure:** Docker, AWS, CI/CD  

---

## 📊 GitHub Stats

<a href="https://github.com/Dancode-188">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api?username=Dancode-188&show_icons=true&theme=radical&cache_bust=true" />
</a>

<a href="https://github.com/Dancode-188">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Dancode-188&layout=compact&theme=radical&langs_count=8&card_width=320" />
</a>

---

## 📫 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-bitengo/)
[![GitHub](https://img.shields.io/badge/Follow-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dancode-188)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:danielbitengo@gmail.com)

---

💡 *Open to consulting opportunities and technical collaborations*
