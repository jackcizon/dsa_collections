from collections.abc import Callable


class BaseRoute:
    """list element"""

    def matches(self, path: str) -> bool:
        raise NotImplementedError()


class Route(BaseRoute):
    """list node"""

    def __init__(self, path: str, endpoint: Callable, name: str) -> None:
        self.path = path
        self.endpoint = endpoint
        self.name = name

    def matches(self, path: str) -> bool:
        return path == self.path

    def __repr__(self) -> str:
        return f"Route(path={self.path!r}, name={self.name!r})"


class Mount(BaseRoute):
    """list pointer"""

    def __init__(self, prefix: str, router: "Router") -> None:
        self.prefix = prefix
        self.router = router

    def matches(self, path: str) -> bool:
        if path.startswith(self.prefix):
            remaining_path = path[len(self.prefix) :]
            return self.router.match(remaining_path)
        return False

    def __repr__(self) -> str:
        return f"Mount(prefix={self.prefix!r}, child_routes={self.router.routes})"


class Router:
    """recursive list"""

    def __init__(self) -> None:
        self._routes: list[BaseRoute] = []

    def add_route(self, path: str, endpoint: Callable, name: str) -> None:
        route = Route(path, endpoint, name)
        self._routes.append(route)

    def include_router(self, router: "Router", prefix: str) -> None:
        mount_point = Mount(prefix, router)
        self._routes.append(mount_point)

    def match(self, path: str) -> bool:
        """recursive search"""
        for route in self._routes:
            if route.matches(path):
                return True
        return False

    def routes(self, base_path: str = "") -> list[tuple[str, str]]:
        """DFS"""
        results: list[tuple[str, str]] = []
        for route in self._routes:
            if isinstance(route, Route):
                # go flatten
                results.append((base_path + route.path, route.name))
            elif isinstance(route, Mount):
                # go deeper, dfs start
                routes = route.router.routes(base_path + route.prefix)
                results.extend(routes)
        return results

    def pprint_routes_tree(self, base_str: str = "/\n", depth: int = 0) -> str:
        r"""
        this is a unix artwork.

        /
        |---auth(Mount)
        |	'--login(Route)
        |	'--register(Route)
        |	'--login(Mount)
        |		'--success(Route)
        |		'--fail(Route)
        |---rbac(Mount)
        |	'--index(Route)

        Note:
        if you replace `Route` -> `File`,
        replace `Mount` -> `Dir`,
        you can see how `tree` works.
        """
        if depth == 0:
            bar = "---"
        else:
            bar = "'--"
        ident = "\t" * depth

        for route in self._routes:
            base_str += "|"
            base_str += ident
            base_str += bar

            if isinstance(route, Route):
                # go flatten
                base_str += route.name
                base_str += "(Route)\n"

            elif isinstance(route, Mount):
                # go deeper, dfs start
                base_str += route.prefix
                base_str += "(Mount)\n"
                sub_str = route.router.pprint_routes_tree("", depth + 1)
                base_str += sub_str

        return base_str


def test_pprint_route_tree() -> None:
    login_router = Router()
    login_router.add_route("success", lambda: None, "success")
    login_router.add_route("fail", lambda: None, "fail")

    auth_router = Router()
    auth_router.add_route("login", lambda: None, "login")
    auth_router.add_route("register", lambda: None, "reg")
    auth_router.include_router(login_router, prefix="login")

    rbac_router = Router()
    rbac_router.add_route("index", lambda: None, "login")

    app_router = Router()
    app_router.include_router(auth_router, prefix="auth")
    app_router.include_router(rbac_router, prefix="rbac")

    print(app_router.pprint_routes_tree())


def test_routes() -> None:
    auth_sub_router = Router()
    auth_sub_router.add_route("/login/", lambda: "ok", "auth:login")
    auth_sub_router.add_route("/register/", lambda: "ok", "auth:reg")

    app_router = Router()
    app_router.include_router(auth_sub_router, prefix="/api/v1/auth")

    print(f"{'FULL PATH':<30} | {'NAME'}")
    print("-" * 45)
    for path, name in app_router.routes():
        print(f"{path:<30} | {name}")

    status = app_router.match("/api/v1/auth/login/")
    print(f"\n match test [/api/v1/auth/login/]: {'success' if status is True else 'fail'}")


if __name__ == "__main__":
    test_routes()
    test_pprint_route_tree()
