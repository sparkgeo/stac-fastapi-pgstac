static_enexus = {
  "type": "Catalog",
  "id": "stac-fastapi",
  "title": "stac-fastapi",
  "description": "stac-fastapi",
  "stac_version": "1.0.0",
  "conformsTo": [
    "http://www.opengis.net/spec/cql2/1.0/conf/basic-cql2",
    "https://api.stacspec.org/v1.0.0/ogcapi-features",
    "https://api.stacspec.org/v1.0.0/item-search#query",
    "https://api.stacspec.org/v1.0.0-rc.2/item-search#filter",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
    "https://api.stacspec.org/v1.0.0/item-search#fields",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "https://api.stacspec.org/v1.0.0-rc.3/ogcapi-features/extensions/transaction",
    "http://www.opengis.net/spec/cql2/1.0/conf/cql2-json",
    "http://www.opengis.net/spec/cql2/1.0/conf/cql2-text",
    "https://api.stacspec.org/v1.0.0-rc.2/item-search#context",
    "https://api.stacspec.org/v1.0.0/item-search",
    "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/filter",
    "https://api.stacspec.org/v1.0.0/core",
    "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter",
    "https://api.stacspec.org/v1.0.0/collections",
    "https://api.stacspec.org/v1.0.0/item-search#sort"
  ],
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "href": "http://localhost:8082/enexus"
    },
    {
      "rel": "root",
      "type": "application/json",
      "href": "http://localhost:8082/"
    },
    {
      "rel": "data",
      "type": "application/json",
      "href": "http://localhost:8082/collections"
    },
    {
      "rel": "conformance",
      "type": "application/json",
      "title": "STAC/WFS3 conformance classes implemented by this server",
      "href": "http://localhost:8082/conformance"
    },
    {
      "rel": "search",
      "type": "application/geo+json",
      "title": "STAC search",
      "href": "http://localhost:8082/search",
      "method": "GET"
    },
    {
      "rel": "search",
      "type": "application/geo+json",
      "title": "STAC search",
      "href": "http://localhost:8082/search",
      "method": "POST"
    },
    {
      "rel": "child",
      "type": "application/json",
      "title": "LP",
      "href": "http://localhost:8082/enexus/lp"
    },
    {
      "rel": "service-desc",
      "type": "application/vnd.oai.openapi+json;version=3.0",
      "title": "OpenAPI service description",
      "href": "http://localhost:8082/api"
    },
    {
      "rel": "service-doc",
      "type": "text/html",
      "title": "OpenAPI service documentation",
      "href": "http://localhost:8082/api.html"
    }
  ],
  "stac_extensions": []
}

static_lp = {
  "type": "Catalog",
  "id": "stac-fastapi",
  "title": "stac-fastapi",
  "description": "stac-fastapi",
  "stac_version": "1.0.0",
  "conformsTo": [
    "http://www.opengis.net/spec/cql2/1.0/conf/basic-cql2",
    "https://api.stacspec.org/v1.0.0/ogcapi-features",
    "https://api.stacspec.org/v1.0.0/item-search#query",
    "https://api.stacspec.org/v1.0.0-rc.2/item-search#filter",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
    "https://api.stacspec.org/v1.0.0/item-search#fields",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "https://api.stacspec.org/v1.0.0-rc.3/ogcapi-features/extensions/transaction",
    "http://www.opengis.net/spec/cql2/1.0/conf/cql2-json",
    "http://www.opengis.net/spec/cql2/1.0/conf/cql2-text",
    "https://api.stacspec.org/v1.0.0-rc.2/item-search#context",
    "https://api.stacspec.org/v1.0.0/item-search",
    "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/filter",
    "https://api.stacspec.org/v1.0.0/core",
    "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter",
    "https://api.stacspec.org/v1.0.0/collections",
    "https://api.stacspec.org/v1.0.0/item-search#sort"
  ],
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "href": "http://localhost:8082/enexus/lp"
    },
    {
      "rel": "root",
      "type": "application/json",
      "href": "http://localhost:8082/"
    },
    {
      "rel": "data",
      "type": "application/json",
      "href": "http://localhost:8082/collections"
    },
    {
      "rel": "conformance",
      "type": "application/json",
      "title": "STAC/WFS3 conformance classes implemented by this server",
      "href": "http://localhost:8082/conformance"
    },
    {
      "rel": "search",
      "type": "application/geo+json",
      "title": "STAC search",
      "href": "http://localhost:8082/search",
      "method": "GET"
    },
    {
      "rel": "search",
      "type": "application/geo+json",
      "title": "STAC search",
      "href": "http://localhost:8082/search",
      "method": "POST"
    },
    {
      "rel": "child",
      "type": "application/json",
      "title": "LP Lidar",
      "href": "http://localhost:8082/collections"
    },
    {
      "rel": "child",
      "type": "application/json",
      "title": "LP Lidar Change",
      "href": "http://localhost:8082/collections"
    },
    {
      "rel": "service-desc",
      "type": "application/vnd.oai.openapi+json;version=3.0",
      "title": "OpenAPI service description",
      "href": "http://localhost:8082/api"
    },
    {
      "rel": "service-doc",
      "type": "text/html",
      "title": "OpenAPI service documentation",
      "href": "http://localhost:8082/api.html"
    }
  ],
  "stac_extensions": []
}