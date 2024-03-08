
def preload(parser):
    parser.add_argument(
        "--civitai-api", 
        type=str, 
        help="Civitai API Key", 
        default=None
    )
    parser.add_argument(
        "--pre-models",
        type=str,
        help="pre download models url file path",
        default=None
    )