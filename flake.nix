{
  description = "Dev shell for Python 3.12";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };

        # Load packages from ./pkgs
        myPkgs = import ./pkgs { inherit pkgs; };
      in {
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = [ pkgs.bashInteractive ];

          buildInputs =
            (with pkgs; [
              # --- Core tools / system --- 
              # Comment out if you dont want this
              vscodium
              positron-bin
              nix-prefetch-git

            ])
            ++ (with pkgs.python312Packages; [
              # --- Python: Core data stack ---
              numpy
              pandas
              polars
              arrow

              # --- Python: Visualization ---
              matplotlib
              seaborn

              # --- Python: Notebook / tooling ---
              ipykernel
              pip
            ]);

          shellHook = ''
            export PYTHONPATH=${toString ./.}/src:$PYTHONPATH
            echo " Environment is set up and ready to use. :D"
          '';
        };
      });
}
