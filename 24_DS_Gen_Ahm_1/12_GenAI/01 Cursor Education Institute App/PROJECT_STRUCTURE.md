# Royal Technosoft ERP — Project Structure (Phase 1)

```
royal-technosoft-erp/
├── .env.example
├── .gitignore
├── components.json              # shadcn/ui (Phase 2)
├── eslint.config.mjs
├── next.config.ts
├── next-env.d.ts
├── package.json
├── postcss.config.mjs
├── PROJECT_STRUCTURE.md         # this file
├── README.md
├── tailwind.config.ts
├── tsconfig.json
│
├── prisma/
│   ├── schema.prisma            # full domain + NextAuth models
│   └── seed.ts                  # bootstrap SUPER_ADMIN
│
└── src/
    ├── middleware.ts            # JWT + RBAC zone enforcement
    │
    ├── types/
    │   ├── next-auth.d.ts       # Session/JWT role extensions
    │   └── rbac.ts              # role ↔ route prefix map
    │
    ├── lib/
    │   ├── auth.ts              # NextAuth options (Credentials + JWT)
    │   ├── auth-guard.ts        # server layout RBAC wrapper
    │   ├── prisma.ts            # Prisma singleton
    │   ├── rbac.ts              # evaluateRouteAccess, requireRoles
    │   ├── session.ts           # getServerSession helper
    │   └── utils.ts             # cn() for shadcn (Phase 2)
    │
    ├── app/
    │   ├── layout.tsx           # root shell (minimal)
    │   ├── page.tsx             # public home (Phase 2)
    │   ├── globals.css
    │   │
    │   ├── api/
    │   │   └── auth/
    │   │       └── [...nextauth]/
    │   │           └── route.ts
    │   │
    │   ├── (auth)/
    │   │   └── login/
    │   │       └── page.tsx     # Phase 2 UI
    │   │
    │   └── (protected)/         # route group — URLs unchanged
    │       ├── super-admin/
    │       │   ├── layout.tsx   # guard: SUPER_ADMIN
    │       │   ├── page.tsx
    │       │   ├── staff/           # Phase 2: CRUD admins, admission, faculty
    │       │   ├── financials/      # Phase 2
    │       │   └── batches/         # Phase 2 global batch dashboard
    │       │
    │       ├── admin/
    │       │   ├── layout.tsx   # guard: ADMIN
    │       │   ├── page.tsx
    │       │   ├── students/
    │       │   ├── faculty/
    │       │   ├── batches/
    │       │   └── certificates/
    │       │
    │       ├── admission/
    │       │   ├── layout.tsx   # guard: ADMISSION
    │       │   ├── page.tsx
    │       │   ├── funnel/          # inquiry CRM, stage moves
    │       │   ├── fees/
    │       │   └── reports/
    │       │
    │       ├── faculty/
    │       │   ├── layout.tsx   # guard: FACULTY
    │       │   ├── page.tsx
    │       │   ├── lectures/        # Jitsi start/end
    │       │   ├── materials/
    │       │   └── assignments/
    │       │
    │       └── student/
    │           ├── layout.tsx   # guard: STUDENT (+ feedback gate Phase 2)
    │           ├── page.tsx
    │           ├── live/            # @jitsi/react-sdk
    │           ├── ide/             # @monaco-editor/react
    │           └── feedback/
    │
    ├── components/              # Phase 2 — shadcn/ui
    │   └── ui/
    │
    ├── hooks/                   # Phase 2
    │
    └── server/                  # Phase 2 — actions, services
        ├── actions/
        └── services/
```

## RBAC routing matrix

| Role         | URL prefix      | Middleware + layout guard |
|--------------|-----------------|---------------------------|
| SUPER_ADMIN  | `/super-admin`  | Yes                       |
| ADMIN        | `/admin`        | Yes                       |
| ADMISSION    | `/admission`    | Yes                       |
| FACULTY      | `/faculty`      | Yes                       |
| STUDENT      | `/student`      | Yes                       |

Public: `/`, `/login`, `/api/auth/*`

## Schema highlights

- **FunnelStage**: `LEAD` → … → `FOLLOWUP_5` → `ADMISSION` (+ `InquiryStageHistory` audit)
- **Batch** ↔ **Subject** via `BatchSubject`; **Enrollment** links students
- **Lecture**: `jitsiRoomId`, `status` (PENDING | LIVE | ENDED)
- **Fee**: `total` / `paid` / `pending`, `FeeStatus` includes `REVOKED` for access revoke
- Supporting: `Assignment`, `Notification`, `FeePayment` (Phase 2 features)
