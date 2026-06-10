import type { Role } from "@prisma/client";
import type { Session } from "next-auth";
import {
  getProtectedPrefix,
  getRoleHomePath,
  isRoleAllowedForPath,
  PUBLIC_ROUTES,
} from "@/types/rbac";

/** Minimal session shape for middleware JWT and server layouts. */
export type AuthSessionLike = Pick<Session, "user"> | null;

export type RbacDecision =
  | { allowed: true }
  | { allowed: false; reason: "unauthenticated" | "inactive" | "forbidden"; redirectTo: string };

function isPublicPath(pathname: string): boolean {
  return PUBLIC_ROUTES.some(
    (route) => pathname === route || pathname.startsWith(`${route}/`),
  );
}

/**
 * Central RBAC check used by middleware and (later) server layouts/actions.
 */
export function evaluateRouteAccess(
  pathname: string,
  session: AuthSessionLike,
): RbacDecision {
  if (isPublicPath(pathname)) {
    return { allowed: true };
  }

  const protectedPrefix = getProtectedPrefix(pathname);
  if (!protectedPrefix) {
    return { allowed: true };
  }

  if (!session?.user?.id) {
    return {
      allowed: false,
      reason: "unauthenticated",
      redirectTo: `/login?callbackUrl=${encodeURIComponent(pathname)}`,
    };
  }

  if (!session.user.isActive) {
    return {
      allowed: false,
      reason: "inactive",
      redirectTo: "/login?error=AccountDeactivated",
    };
  }

  const role = session.user.role;
  if (!isRoleAllowedForPath(role, pathname)) {
    return {
      allowed: false,
      reason: "forbidden",
      redirectTo: getRoleHomePath(role),
    };
  }

  return { allowed: true };
}

/** Type-safe role guard for server actions / API routes. */
export function requireRoles(
  session: Session | null,
  allowed: Role[],
): asserts session is Session & { user: { role: Role } } {
  if (!session?.user?.id) {
    throw new Error("UNAUTHORIZED");
  }
  if (!session.user.isActive) {
    throw new Error("ACCOUNT_INACTIVE");
  }
  if (!allowed.includes(session.user.role)) {
    throw new Error("FORBIDDEN");
  }
}
