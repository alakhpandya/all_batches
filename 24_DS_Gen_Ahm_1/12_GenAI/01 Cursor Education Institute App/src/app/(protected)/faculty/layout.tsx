import { guardProtectedLayout } from "@/lib/auth-guard";

export default async function FacultyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  await guardProtectedLayout("/faculty", ["FACULTY"]);
  return children;
}
