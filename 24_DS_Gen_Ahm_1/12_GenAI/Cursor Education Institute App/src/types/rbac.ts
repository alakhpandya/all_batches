import type { Role } from "@prisma/client";

/** URL prefix for each protected layout zone (App Router segment). */
export const ROLE_ROUTE_PREFIX: Record<Role, string> = {
  SUPER_ADMIN: "/super-admin",
  ADMIN: "/admin",
  ADMISSION: "/admission",
  FACULTY: "/faculty",
  STUDENT: "/student",
} as const;

/** Roles allowed to access a given route prefix (exact match on first segment). */
export const ROUTE_PREFIX_ALLOWED_ROLES: Record<string, Role[]> = {
  "/super-admin": ["SUPER_ADMIN"],
  "/admin": ["ADMIN"],
  "/admission": ["ADMISSION"],
  "/faculty": ["FACULTY"],
  "/student": ["STUDENT"],
};

export const PROTECTED_ROUTE_PREFIXES = Object.keys(
  ROUTE_PREFIX_ALLOWED_ROLES,
) as (keyof typeof ROUTE_PREFIX_ALLOWED_ROLES)[];

export const PUBLIC_ROUTES = ["/", "/login", "/api/auth"] as const;

export function getRoleHomePath(role: Role): string {
  return ROLE_ROUTE_PREFIX[role];
}

export function isRoleAllowedForPath(role: Role, pathname: string): boolean {
  const prefix = PROTECTED_ROUTE_PREFIXES.find((p) =>
    pathname.startsWith(p),
  );
  if (!prefix) return false;
  return ROUTE_PREFIX_ALLOWED_ROLES[prefix]?.includes(role) ?? false;
}

export function getProtectedPrefix(pathname: string): string | null {
  return (
    PROTECTED_ROUTE_PREFIXES.find((p) => pathname.startsWith(p)) ?? null
  );
}
