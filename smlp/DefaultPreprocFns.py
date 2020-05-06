'''
Copyright 2020, IBM CORP.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors      : Nikolas Ioannou,

End Copyright
'''

import numpy as np

def default_np_preproc_fn(X_y, column_idx: int):
    # assumes label is at the first column
    y = X_y[:, column_idx] #  First column or Get the ML-IO ``Tensor`` of the column called 'label'.
    X_y = np.delete(X_y, column_idx, 1) # array, idx, axis (0 row, 1 column)
    return X_y, y
