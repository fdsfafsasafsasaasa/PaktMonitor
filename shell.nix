with import <nixpkgs> {}; 
mkShell { 
    buildInputs = [ (python3.withPackages (p: with p; [ 
        flask 
        pymongo ]
        )) ]; 
    }