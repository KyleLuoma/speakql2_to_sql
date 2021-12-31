class TableSourceItem:

    def __init__(self):
        self.name = ""
        self.alias = ""

    def set_name(self, new_name):
        self.name = new_name.strip()

    def set_alias(self, new_alias):
        self.alias = new_alias.strip()

    def get_name(self):
        return self.name

    def get_alias(self):
        return self.alias

    def get_alias_if_exists_else_name(self):
        if self.has_alias(): return self.alias
        elif self.has_name(): return self.name
        else: return ""

    def has_alias(self):
        return len(self.alias) > 0

    def has_name(self):
        return len(self.name) > 0

    def to_string(self):
        return "tableName: " + self.name + ", tableAlias: " + self.alias

    def as_list(self):
        return [self.name, self.alias]

    def as_dict(self):
        return {"name" : self.name, "alias" : self.alias}

    def as_sql_fragment(self):
        sql_fragment = self.name
        if self.has_alias():
            sql_fragment = sql_fragment + " AS " + self.alias
        return sql_fragment
