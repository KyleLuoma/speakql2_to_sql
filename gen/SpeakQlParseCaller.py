import subprocess

def run_select_statement():
    output = subprocess.run(
        "java org.antlr.v4.gui.TestRig SpeakQl selectStatement -inputFile \"../query.txt\" -tree", 
        capture_output=True,
        cwd="c:/research_projects/speakql2_to_sql/gen/"
        )
    return output