import { redirect } from "next/navigation";
import type { Role } from "@prisma/client";
import { getSession } from "@/lib/session";
import { evaluateRouteAccess } from "@/lib/rbac";
import { getRoleHomePath } from "@/types/rbac";

/**
 * Server Component layout guard — mirrors middleware RBAC for defense in depth.
 * Call from each protected zone's layout.tsx (Phase 2+).
 */
export async function guardProtectedLayout(
  routePrefix: string,
  allowedRoles: Role[],
) {
  const session = await getSession();
  const decision = evaluateRouteAccess(routePrefix, session);

  if (!decision.allowed) {
    redirect(decision.redirectTo);
  }

  if (session && !allowedRoles.includes(session.user.role)) {
    redirect(getRoleHomePath(session.user.role));
  }

  return session;
}
