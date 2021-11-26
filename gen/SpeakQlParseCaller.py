import subprocess

def run_select_statement():
    output = subprocess.run(
        "java org.antlr.v4.gui.TestRig SpeakQl selectStatement -inputFile \"../../query.txt\" -tree", 
        capture_output=True,
        cwd="c:/research_projects/speakql2_to_sql/antlr_builds/gen_increased_query_specification_var"
        )
    return output