from stac_fastapi.pgstac.static_response import static_enexus, static_lp
from stac_fastapi.api.app import StacApi
from fastapi import APIRouter


class StacApiEnexus(StacApi):
    """
    Extended the stac-fastapi Class to add more endpoints
    """

    def add_enexus(self):
        """Test Endpoint"""
        mgmt_router = APIRouter(prefix=self.app.state.router_prefix)

        @mgmt_router.get("/enexus")
        async def enexus():
            """static response for nesting"""
            return static_enexus

        self.app.include_router(mgmt_router, tags=["Static Responses for STAC Browser (Catalog Nesting)"])

    def add_lp(self):
        """Test Endpoint"""
        mgmt_router = APIRouter(prefix=self.app.state.router_prefix)

        @mgmt_router.get("/enexus/lp")
        async def lp():
            """static response for nesting"""
            return static_lp

        self.app.include_router(mgmt_router, tags=["Static Responses for STAC Browser (Catalog Nesting)"])

    # def add_lp_lidar(self):
    #     """Test Endpoint"""
    #     mgmt_router = APIRouter(prefix=self.app.state.router_prefix)

    #     @mgmt_router.get("/enexus/lp/lp-lidar")
    #     async def lp_lidar():
    #         """static response for nesting"""
    #         return static_enexus

    #     self.app.include_router(mgmt_router, tags=["Static Responses for STAC Browser (Catalog Nesting)"])

    # def add_lp_lidar_change(self):
    #     """Test Endpoint"""
    #     mgmt_router = APIRouter(prefix=self.app.state.router_prefix)

    #     @mgmt_router.get("/enexus/lp/lp-lidar-change")
    #     async def lp_lidar_change():
    #         """static response for nesting"""
    #         return static_enexus

    #     self.app.include_router(mgmt_router, tags=["Static Responses for STAC Browser (Catalog Nesting)"])
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.add_enexus()
        self.add_lp()
        # self.add_lp_lidar()
        # self.add_lp_lidar_change()