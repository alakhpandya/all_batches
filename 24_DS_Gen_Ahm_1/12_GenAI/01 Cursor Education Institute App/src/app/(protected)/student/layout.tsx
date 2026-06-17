import { guardProtectedLayout } from "@/lib/auth-guard";

export default async function StudentLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  await guardProtectedLayout("/student", ["STUDENT"]);
  return children;
}
