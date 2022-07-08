from ovito.io import import_file
from ovito.modifiers import CoordinationAnalysisModifier
import numpy
from sys import argv

# Load a simulation trajectory consisting of several frames:
pipeline = import_file("traj.xyz")

# Insert the modifier into the pipeline:
modifier = CoordinationAnalysisModifier(cutoff = 3.0, number_of_bins = 50)
pipeline.modifiers.append(modifier)

# Initialize array for accumulated RDF histogram to zero:
total_rdf = numpy.zeros((modifier.number_of_bins, 2))

# Iterate over all frames of the sequence.
for frame in range(pipeline.source.num_frames):
    # Evaluate pipeline to let the modifier compute the RDF of the current frame:
    data = pipeline.compute(frame)
    # Accumulate RDF histograms:
    total_rdf += data.tables['coordination-rdf'].xy()

# Averaging:
total_rdf /= pipeline.source.num_frames

# Export the average RDF to a text file:
numpy.savetxt("rdf.txt", total_rdf)
