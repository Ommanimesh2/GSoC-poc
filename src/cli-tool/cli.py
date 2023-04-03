import argparse
from ogcapi.api import OgcApi


def main():
    parser = argparse.ArgumentParser(description='OGC API CLI')
    parser.add_argument('--url', required=True, help='Base URL of the OGC API')
    parser.add_argument('--collection', help='Name of the collection')
    parser.add_argument('--feature', help='ID of the feature')
    parser.add_argument('--property', help='Name of the property')
    parser.add_argument('--value', help='Value of the property')

    args = parser.parse_args()

    api = OgcApi(args.url)

    if args.collection:
        if args.feature:
            if args.property and args.value:
                api.update_feature_property(args.collection, args.feature, args.property, args.value)
            else:
                api.get_feature(args.collection, args.feature)
        else:
            api.get_collection(args.collection)


if __name__ == '__main__':
    main()
