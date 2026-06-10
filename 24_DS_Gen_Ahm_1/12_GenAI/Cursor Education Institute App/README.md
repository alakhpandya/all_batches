# Royal Technosoft — Ed-Tech ERP

Phase 1 delivers the data model, NextAuth (Credentials + JWT), and RBAC middleware. UI is Phase 2.

## Stack

- Next.js 15 (App Router, TypeScript)
- Tailwind CSS + shadcn/ui (configured, components in Phase 2)
- Prisma + PostgreSQL
- NextAuth v4 with role-based access control

## Quick start

```bash
cp .env.example .env
# Set DATABASE_URL and NEXTAUTH_SECRET

npm install
npx prisma db push
npm run db:generate
npx tsx prisma/seed.ts   # optional: superadmin@royaltechnosoft.com / ChangeMe123!

npm run dev
```

## Auth flow

1. `POST /api/auth/callback/credentials` via NextAuth `signIn("credentials", …)`.
2. JWT carries `id`, `role`, `isActive`.
3. `src/middleware.ts` enforces zone access; each `(protected)/*/layout.tsx` re-validates server-side.

See [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) for the full tree and Phase 2 route plan.
