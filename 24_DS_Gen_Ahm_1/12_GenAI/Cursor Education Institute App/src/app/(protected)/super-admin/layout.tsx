import { guardProtectedLayout } from "@/lib/auth-guard";

export default async function SuperAdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  await guardProtectedLayout("/super-admin", ["SUPER_ADMIN"]);
  return children;
}
