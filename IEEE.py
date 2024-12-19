class IEEECitation:
    def __init__(self, authors, title, year, source_type, publisher=None):
        self.authors = authors
        self.title = title
        self.year = year
        self.source_type = source_type
        self.publisher = publisher

    def format_citation(self):
        authors_formatted = " & ".join(self.authors)
        if self.source_type == "journal":
            citation = f"{authors_formatted}, \"{self.title},\" {self.source_type.capitalize()}, vol. X, no. X, pp. XX-XX, {self.year}."
        elif self.source_type == "book":
            citation = f"{authors_formatted}, *{self.title}*, {self.publisher}, {self.year}."
        elif self.source_type == "conference":
            citation = f"{authors_formatted}, \"{self.title},\" in *Proceedings of the Conference Name*, {self.year}, pp. XX-XX."
        else:
            citation = "Invalid source type."

        return citation

# Ejemplos de uso
source1 = IEEECitation(["Author1", "Author2"], "Title of Journal Article", "2023", "journal")
source2 = IEEECitation(["Author3"], "Title of Book", "2022", "book", publisher="Book Publisher")
source3 = IEEECitation(["Author4", "Author5", "Author6"], "Title of Conference Paper", "2023", "conference")

print(source1.format_citation())
print(source2.format_citation())
print(source3.format_citation())
