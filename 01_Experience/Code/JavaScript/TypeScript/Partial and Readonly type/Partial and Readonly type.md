# Partial
- `Partial` type set all properties of an object/interface optional

```ts
interface CourseGoal {
    title: string;
    description: string;
    completeUntil: Date;
}

function createCourseGoal(
    title: string,
    description: string,
    date: Date
): CourseGoal {
    let courseGoal: Partial<CourseGoal> = {};
    // Partial set all properties of CourseGoal to optional
    courseGoal.title = title;
    courseGoal.description = description;
    courseGoal.completeUntil = date;
    return courseGoal as CourseGoal;
}
```

# Readonly
- `Readonly` type prevents object being modified after initiated

```ts
const names: Readonly<string[]> = ['Max', 'Anna'];
// name cannot be modified
```

# 

---
- Status: #done

- Tags: #js

- References:
	- 

- Related:
	- 
