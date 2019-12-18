import hyphen


def load_modules():
    hyphen.importing.EXPECTED_EMPTY += ['Database', 'Database.Sql','Database.Sql.Util', 'Database.Sql.Vertica', 'Demo', 'Text', 'Text.PrettyPrint.HughesPJ.Doc' ]
    import hs.Demo
    import hs.Data.Text.Lazy
    import hs.Text.PrettyPrint.HughesPJ
    query = hs.Data.Text.Lazy.fromChunks(["SELECT * from foo"])
    result = hs.Demo.demoAllAnalyses(query)
    return hs.Text.PrettyPrint.HughesPJ.render(result)

print(load_modules())
