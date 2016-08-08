#!/usr/bin/env bash

# Run wxklsyn.pyw in the Python 2.7 environment.
    bash << EOF
    source /home/ubuntu/miniconda3/bin/activate py27
    wxklsyn.pyw
    source deactivate
EOF

