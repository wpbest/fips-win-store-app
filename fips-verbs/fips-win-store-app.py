"""verb import test"""

from mod import log

#-------------------------------------------------------------------------------
def run(proj_dir, fips_dir, args) :
    log.info("fips-win-store-app test verb executed")

#-------------------------------------------------------------------------------
def help() :
    log.info(log.YELLOW +
            "fips fips-win-store-app\n"
            + log.DEF +
            "    test an imported project verb")
