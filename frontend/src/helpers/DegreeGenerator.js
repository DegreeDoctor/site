export function degreeGenerator(degree, programsData, coursesData) {
    let template = {};
    for (const i in degree["majors"]) {
        let temp = programsData["2022-2023"][degree["majors"][i]]["template"];
        for (const sem in temp) {
            if (!template[sem]) {
                template[sem] = [];
            }
            const courses = temp[sem];
            template[sem] = [...template[sem], ...courses];
        }
    }

    for (const sem in template) {
        template[sem] = [...new Set(template[sem])];
        for (const sem2 in template) {
            if (sem == sem2) continue;
            template[sem] = template[sem].filter(
                (c) => !template[sem2].includes(c)
            );
        }
    }

    // Convert template to using course objects
    for (const sem in template) {
        let courses = template[sem];
        let newCourses = [];
        for (const i in courses) {
            if (coursesData[courses[i]]) {
                newCourses.push(coursesData[courses[i]]);
            }
        }
        template[sem] = newCourses;
    }

    //seperate "labels" from semesters and change courses to array of arrays
    let semesters = [];
    let labels = [];
    for (const sem in template) {
        labels.push(sem);
        semesters.push(template[sem]);
    }

    let remainder = [];
    let newSemesters = [];
    let coursesTaken = [];
    for (const i in semesters) {
        let coursesToAdd = [...semesters[i], ...remainder];
        remainder = [];

        for (const j in semesters[i]) {
            let course = semesters[i][j];
            if (course["prerequisites"].length != 0) {
                const reqs = course["prerequisites"]["required"];
                let pushed_back = false;
                for (const k in reqs) {
                    let prereq = reqs[k];
                    for (const l in semesters[i]) {
                        if (
                            semesters[i][l]["name"].toLowerCase() ===
                                prereq.toLowerCase() &&
                            semesters[i][l]["name"] !== course["name"]
                        ) {
                            //if the other course has this course as a prereq, ignore it
                            let otherCourse = semesters[i][l];
                            if (otherCourse["prerequisites"].length != 0) {
                                const otherReqs =
                                    otherCourse["prerequisites"]["required"];
                                let needBreak = false;
                                for (const m in otherReqs) {
                                    if (
                                        otherReqs[m].toLowerCase() ===
                                        course["name"].toLowerCase()
                                    ) {
                                        needBreak = true;
                                        break;
                                    }
                                }
                                if (needBreak) break;
                            }
                            remainder.push(semesters[i][j]);
                            coursesToAdd = coursesToAdd.filter(
                                (c) => c["name"] !== course["name"]
                            );
                            pushed_back = true;
                        }
                    }
                }
                if (pushed_back) continue;

                const one_of = course["prerequisites"]["one_of"];
                let one_of_taken = false;
                for (const k in one_of) {
                    let prereq = one_of[k];
                    for (const l in coursesTaken) {
                        if (
                            coursesTaken[l]["name"].toLowerCase() ===
                            prereq.toLowerCase()
                        ) {
                            one_of_taken = true;
                        }
                    }
                }
                if (one_of_taken) continue;

                for (const k in one_of) {
                    let prereq = one_of[k];
                    for (const l in semesters[i]) {
                        if (
                            semesters[i][l]["name"].toLowerCase() ===
                                prereq.toLowerCase() &&
                            semesters[i][l]["name"] !== course["name"]
                        ) {
                            remainder.push(semesters[i][j]);
                            coursesToAdd = coursesToAdd.filter(
                                (c) => c["name"] !== course["name"]
                            );
                        }
                    }
                }
            }
        }

        let credits = 0;
        for (const j in coursesToAdd) {
            let course = coursesToAdd[j];
            credits += course["credits"][0];
        }

        //sort courses to add by amount of prereqs
        coursesToAdd.sort((a, b) => {
            if (
                a["prerequisites"].length == 0 &&
                b["prerequisites"].length == 0
            ) {
                return 0;
            }
            if (a["prerequisites"].length == 0) return 1;
            if (b["prerequisites"].length == 0) return -1;

            let aPrereqs = [
                ...a["prerequisites"]["required"],
                ...a["prerequisites"]["one_of"],
            ];
            let bPrereqs = [
                ...b["prerequisites"]["required"],
                ...b["prerequisites"]["one_of"],
            ];
            return bPrereqs.length - aPrereqs.length;
        });

        while (credits > 18) {
            let course = coursesToAdd.pop();
            remainder.push(course);
            credits -= course["credits"][0];
        }

        coursesTaken = [...coursesTaken, ...coursesToAdd];
        newSemesters.push(coursesToAdd);
    }

    if (remainder.length > 0) {
        console.log("Error: Not enough semesters to complete degree");
    }

    semesters = newSemesters;

    //convert back to object
    template = {};
    for (const i in semesters) {
        //convert semester to just course names
        let courses = semesters[i];
        let newCourses = [];
        for (const j in courses) {
            newCourses.push(courses[j]["name"]);
        }
        semesters[i] = newCourses;
        template[labels[i]] = semesters[i];
    }

    degree["template"] = template;
    return degree;
}
