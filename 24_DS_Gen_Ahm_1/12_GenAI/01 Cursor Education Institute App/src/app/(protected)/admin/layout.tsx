import { guardProtectedLayout } from "@/lib/auth-guard";

export default async function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  await guardProtectedLayout("/admin", ["ADMIN"]);
  return children;
}
