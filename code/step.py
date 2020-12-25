import numpy as np
import h5py

with h5py.File(
    "/Users/saeedkazemi/Documents/reproducible-research/data/colourvideo_seg.h5", "r"
) as hdf:
    items = list(hdf.items())
    print(items)

    barefoot = hdf.get("surveydata")
    items = list(barefoot.items())
    print(items)

    w2 = barefoot.get("slow")
    items = list(w2.items())
    print(items)

    data = np.array(barefoot.get("data"))
    print(data.shape)
    metadata = np.array(barefoot.get("metadata"))
    print(metadata.shape)
    timestamps = np.array(barefoot.get("timestamps"))
    print(timestamps.shape)
    print(metadata)
