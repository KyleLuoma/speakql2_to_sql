f = open("C:/research_projects/speakql2_to_sql/artifacts/token_permutation/single_join_expression_tokens.spql", "r")
f_out = open("./single_join_expression_tokens_no_duplicates.spql", "w")

last_line = ""

for line in f:
    if not last_line ==  line:
        f_out.write(line)
    last_line = line

