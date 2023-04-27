import course_scraper, minor_scraper, sis_scraper, program_scraper, pathway_scraper
if __name__ == "__main__":
    course_scraper.scrape_courses()
    minor_scraper.scrape_minors()
    program_scraper.scrape_programs()
    pathway_scraper.scrape_pathways()
    sis_scraper.sis_scraper()