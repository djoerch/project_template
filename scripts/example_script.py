#!/usr/bin/env python

import os

from argparse import ArgumentParser, RawTextHelpFormatter  # noqa: E402
from textwrap import dedent  # noqa: E402

from example_package.log_utils import (  # noqa: E402
    add_verbosity_options_to_argparser,
    get_logger,
    log_lvl_from_verbosity_args,
)


PARTICIPANT = "participant"
GROUP = "group"


DESC = dedent(
    """
    Run pipeline on BIDS dataset.
    """
)
EPILOG = dedent(
    """
    Example call:
      {filename} --dataroot /path/to/bids/dataset --derivatives-outputroot /path/to/derivatives --analysis {participant} {group} --cachefolder /path/to/cachefolder
    """.format(  # noqa: E501
        filename=os.path.basename(__file__),
        participant=PARTICIPANT,
        group=GROUP,
    )
)


def build_argparser():

    p = ArgumentParser(
        description=DESC, epilog=EPILOG, formatter_class=RawTextHelpFormatter
    )
    p.add_argument(
        "-i",
        "--dataroot",
        required=True,
        help="Path to BIDS root folder.",
    )
    p.add_argument(
        "-o",
        "--derivatives-outputroot",
        required=True,
        help="Path to root folder for all derivatives output.",
    )
    p.add_argument(
        "--cachefolder",
        required=True,
        help="Path to the root of the cache folder for all workflow cache output.",
    )
    p.add_argument(
        "--participant-label",
        type=str,
        required=False,
        default=None,
        nargs="*",
        help="Restrict computation to the specified subset of subject ids.",
    )
    p.add_argument(
        "--analysis",
        required=True,
        choices={PARTICIPANT, GROUP},
        nargs="+",
        help="Level of analyses."
        f" '{PARTICIPANT}' - individual subject computations;"
        f" '{GROUP}' - execute ONLY results aggregation over"
        " all participants",
    )
    p.add_argument(
        "--pipeline-config",
        type=str,
        required=False,
        help="Path to .yml config file to configure steps of the pipeline.",
    )
    add_verbosity_options_to_argparser(p)

    return p


def main():

    # get command line arguments
    p = build_argparser()
    args = vars(p.parse_args())

    logger = get_logger(
        name=os.path.basename(__file__),
        level=log_lvl_from_verbosity_args(args),
    )

    # assert that all paths are given as absolute paths
    args["dataroot"] = os.path.abspath(args["dataroot"])
    args["derivatives_outputroot"] = os.path.abspath(args["derivatives_outputroot"])
    args["cachefolder"] = os.path.abspath(args["cachefolder"])
    if args["pipeline_config"]:
        args["pipeline_config"] = os.path.abspath(args["pipeline_config"])

    logger.info("Reading BIDS dataset at '{}'.".format(args["dataroot"]))
    logger.info("Analysis level: '{}'.".format(args["analysis"]))

    # TODO: add more code here


if __name__ == "__main__":
    main()
