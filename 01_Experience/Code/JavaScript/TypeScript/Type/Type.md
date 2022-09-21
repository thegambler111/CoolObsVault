# alias

```ts
type CalculationResults = { res: number; print: () => void }[];
// type CalculationResults requires properties 'res' and method 'print'
let results: CalculationResults = [];
// all element in results must have type CalculationResults
```

# Union
```ts
let printMode: 'console' | 'alert';
// printMode value can only be either 'console' or 'alert'
```

# Intersect
```ts
type Combinable = string | number;
type Numeric = number | boolean;
type Universal = Combinable & Numeric;
// `Universal` is intersection of `Combinable` and `Numeric` => number 
```

# Enum
```ts
type PrintMode = OutputMode.ALERT | OutputMode.CONSOLE;
enum OutputMode {
    CONSOLE,
    ALERT,
}
let printMode: PrintMode;
if (printMode === OutputMode.ALERT) {
	...
}

```

# Interface
- Interface can be used as type declaration

```ts
type CalculationResults = { res: number; print: () => void }[];

// Below code is equal to above code
interface CalculatorContainer {
    res: number;
    print(): void;
}

type CalculationResults = CalculatorContainer[];
//=====

let results: CalculationResults = [];
// OR
let results2: Array<CalculationResults> = [];

```

# Type guard
- You can use `in` to check if object has a specific property or function

```ts
type Admin = {
    name: string;
    privileges: string[];
};

type Employee = {
    name: string;
    startDate: Date;
};

type UnknownEmployee = Employee | Admin;

function printEmployeeInfo(emp: UnknownEmployee) {
    console.log('Name: ' + emp.name);
    if ('privileges' in emp) {
        console.log('Privileges: ' + emp.privileges);
    }
    if ('startDate' in emp) {
        console.log('Start Date: ' + emp.startDate);
    }
}

```

- You can also using `instanceof` to check if an object is of a certain `class`

```ts
class Car {
    drive() {
        console.log('Driving...');
    }
}

class Truck {
    drive() {
        console.log('Driving a truck...');
    }

    loadCargo(amount: number) {
        console.log('Loading cargo... ' + amount);
    }
}

type Vehicle = Car | Truck;

function useVehicle(vehicle: Vehicle) {
    vehicle.drive();
    if (vehicle instanceof Truck) {
        vehicle.loadCargo(1000);
    }
}
```
# Type casting
- You can define type of DOM element using `as` or `<>`

```ts
const userInputElement = <HTMLInputElement>(
    document.getElementById('user-input')!
);
// =====
const userInputElement = document.getElementById(
    'user-input'
) as HTMLInputElement;
```

# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
