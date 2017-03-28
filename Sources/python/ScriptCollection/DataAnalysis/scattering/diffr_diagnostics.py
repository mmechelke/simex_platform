#!/usr/bin/env python2.7

from SimEx.Analysis.DiffractionAnalysis import DiffractionAnalysis, plt

from argparse import ArgumentParser
import numpy


def main(args=None):

    # Setup the object.
    analyzer = DiffractionAnalysis(input_path=args.input_path,
                                   pattern_indices=eval(args.pattern_indices),
                                   poissonize=eval(args.poissonize),
                                   )


    # Plot if requested.
    if args.plot:
        analyzer.plotPattern(logscale=args.logscale,
                             operation=eval(args.operation),
                             )
        plt.show()

    # Animate if requested.
    if args.animation_filename:
        analyzer.animatePatterns(output_path=args.animation_filename)

        print "Animated gif saved to %s." % (analyzer._DiffractionAnalysis__animation_output_path)



if __name__ == '__main__':

    # Setup argument parser.
    parser = ArgumentParser()

    # Add arguments.
    parser.add_argument("input_path",
                        metavar="input_path",
                        help="Name (path) of input file (dir).",
                        default=None)

    parser.add_argument("-p",
                        "--pattern_indices",
                        dest="pattern_indices",
                        default="None",
                        help="")

    parser.add_argument("-P",
                        "--plot",
                        action="store_true",
                        dest="plot",
                        default=False,
                        help="Flag indicating whether to render a plot or not.")

    parser.add_argument("-l",
                        "--logscale",
                        action="store_true",
                        dest="logscale",
                        default=False,
                        help="Apply logscale to z-axis in color profiles.")

    parser.add_argument("-a",
                        "--animation",
                        dest="animation_filename",
                        default="",
                        help="Generate an animated gif out of the given patterns and save to given filename.")

    parser.add_argument("-o",
                        "--operation",
                        dest="operation",
                        default="numpy.sum",
                        help="Which operation to apply to a pattern sequence before plotting.")

    parser.add_argument("-z",
                        "--poissonize",
                        dest="poissonize",
                        default=True,
                        help="Whether to read the poissonized diffraction photon numbers (True) or diffraction intensities (False).")

    # Parse arguments.
    args = parser.parse_args()

    # Call main with arguments.
    main(args)
