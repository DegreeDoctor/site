export function degreeGenerator (degree, programsData, coursesData) {
    /* Degree is formatted as follows
        "name" {
            //Credits
            // Object of lists formatted as: {"course1": 4, "Course2", 3}
            credits   {},
            //Name of degree user defined
            name: "",
            //List of major names
            majors: [],
            //List of minor names
            minors: [],
            //Name of pathway
            pathway: "",
            //Name of concentration
            concentration: "",
            // Template see program_template_specs.json in backend for it
            template: {
                // Each Semester labeled by number for year and name of semester
                // Contains a list of courses
                1-Fall: [
                ],
            }
        }
    */

    /*
    COurse looks like the following
    "Introduction to Cellular and Molecular Biology Laboratory": {
        "ID": "2125",
        "credits": [1],
        "crosslisted": {},
        "description": "The goal of this course is to gain practical experience with cellular and molecular biology through handson experimental techniques The laboratory exercises are designed to illustrate current concepts in cellular and molecular biology",
        "name": "Introduction to Cellular and Molecular Biology Laboratory",
        "offered": {
            "semesters": ["fall", "spring", "summer"],
            "year": "all"
        },
        "prerequisites": {
            "one_of": [],
            "required": ["BIOL-2120", "BIOL-1010"]
        },
        "professors": [],
        "properties": {
            "CI": false,
            "MR": false
        },
        "subject": "BIOL"
    },
    */

    let template = {};
    for(const i in degree["majors"]) {
        let temp = programsData["2022-2023"][degree["majors"][i]]["template"];
        for(const sem in temp) {
            if(!template[sem]) {
                template[sem] = [];
            }
            const courses = temp[sem];
            template[sem] = [...template[sem], ...courses];
        }
    }
    
    for(const sem in template) {
        template[sem] = [...new Set(template[sem])];
    }

    // Convert template to using course objects
    for(const sem in template) {
        let courses = template[sem];
        let newCourses = [];
        for(const i in courses) {
            if(coursesData[courses[i]]) {
                newCourses.push(coursesData[courses[i]]);
            }
        }
        template[sem] = newCourses;
    }

    //seperate "labels" from semesters and change courses to array of arrays
    let semesters = [];
    let labels = [];
    for(const sem in template) {
        labels.push(sem);
        semesters.push(template[sem]);
    }

    let coursesToClear = [];
    for(const i in semesters) {
        //add coursesToClear to this semester
        console.log(JSON.parse(JSON.stringify(labels[i])));
        console.log(JSON.parse(JSON.stringify(coursesToClear)));
        semesters[i] = [...semesters[i], ...coursesToClear];
        coursesToClear = [];

        console.log(JSON.parse(JSON.stringify(semesters[i])));
        for(const j in semesters[i]) {
            let course = semesters[i][j];
            let prereqs = course["prerequisites"]["required"];
            for(const c in course["prerequisites"]["one_of"]) {
                prereqs = [...prereqs, ...course["prerequisites"]["one_of"][c]];
            }

            for(const k in prereqs) {
                let prereq = prereqs[k];
                for(const l in semesters[i]) {
                    if(semesters[i][l]["name"] === prereq) {
                        console.log(semesters[i][j]);
                        coursesToClear.push(semesters[i][j]);
                        semesters[i+1].push(semesters[i][j]);
                    }
                }
            }
        }

        for(const j in coursesToClear) {
            let course = coursesToClear[j];
            semesters[i] = semesters[i].filter((c) => c["name"] !== course["name"]);
        }
        coursesToClear = [];

        let credits = 0;
        for(const j in semesters[i]) {
            let course = semesters[i][j];
            credits += course["credits"][0];
        }

        while(credits > 18) {
            let course = semesters[i].pop();
            coursesToClear.push(course);
            credits -= course["credits"][0];
        }
    }

    if(coursesToClear.length > 0) {
        console.log("Error: Not enough semesters to complete degree");
    }

    //convert back to object
    template = {};
    for(const i in semesters) {
        //convert semester to just course names
        let courses = semesters[i];
        let newCourses = [];
        for(const j in courses) {
            newCourses.push(courses[j]["name"]);
        }
        semesters[i] = newCourses;
        template[labels[i]] = semesters[i];
    }

    degree["template"] = template;
    return degree;
}