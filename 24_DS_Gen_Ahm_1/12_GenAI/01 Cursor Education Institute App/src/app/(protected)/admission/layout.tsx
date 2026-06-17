import { guardProtectedLayout } from "@/lib/auth-guard";

export default async function AdmissionLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  await guardProtectedLayout("/admission", ["ADMISSION"]);
  return children;
}
