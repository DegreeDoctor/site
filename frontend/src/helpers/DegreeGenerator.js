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
    "Computer Science I": {
        "ID": "1100",
        "credits": [4],
        "crosslisted": {},
        "description": "An introduction to computer programming algorithm design and analysis Additional topics include basic computer organization internal representation of scalar and array data use of topdown design and subprograms to tackle complex problems abstract data types Enrichment material as time allows Interdisciplinary case studies numerical and nonnumerical applications Students who have passed CSCI 1200 cannot register for this course",
        "name": "Computer Science I",
        "offered": {
            "semesters": ["fall", "spring", "summer"],
            "year": "all"
        },
        "prerequisites": [],
        "professors": [],
        "properties": {
            "CI": false,
            "MR": false
        },
        "subject": "CSCI"
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

    // Push back courses such that the user doesn't take more than 16 credits in a semester
    let pushCourses = [];
    for(const sem in template) {
        // add push courses to the semester
        template[sem] = [...template[sem], ...pushCourses];
        pushCourses = [];
        //push back prerequistes courses
        let toRemove = [];
        for(const i in template[sem]) {
            const prereqs = template[sem][i]["prerequisites"];
            for(const j in prereqs) {
                let idx = template[sem].indexOf(prereqs[j]);
                if(idx != -1) {
                    pushCourses.push(template[sem][idx]);
                    //remove course
                    toRemove.push(template[sem][idx]["name"]);
                }
            }
        }

        for(const i in toRemove) {
            let idx = template[sem].indexOf(toRemove[i]);
            if(idx != -1) {
                template[sem].splice(idx, 1);
            }
        }

        
        let courses = template[sem];
        toRemove = [];
        let credits = 0;
        for(const i in courses) {
            credits += courses[i]["credits"][0];
            if(credits > 18) {
                pushCourses.push(courses[i]);
                credits -= courses[i]["credits"][0];
                toRemove.push(courses[i]["name"]);
            }
        }
        for(const i in toRemove) {
            let idx = template[sem].indexOf(toRemove[i]);
            if(idx != -1) {
                template[sem].splice(idx, 1);
            }
        }
    }
    if(pushCourses.length > 0) {
        console.log("Error: Degree is not possible");
    }

    //Convert templater back to course names
    for(const sem in template) {
        let courses = template[sem];
        let newCourses = [];
        for(const i in courses) {
            newCourses.push(courses[i]["name"]);
        }
        template[sem] = newCourses;
    }


    degree["template"] = template;
    return degree;
}