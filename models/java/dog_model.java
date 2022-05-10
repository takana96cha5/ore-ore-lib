class Dog {
    public String name;
    public int size;
    public int age;

    public Dog(String name, int size, int age) {
        this.name = name;
        this.size = size;
        this.age = age;
    }

    public String bark() {
       if (size >= 50) return "Wooof! Woof!";
       else if (size >= 20) return "Ruff! Ruff!";
       else return "Yip! Yip!";
    }

    public int calcHumanAge() {
        return (age - 1) * 7 + 12;
    }
}

class MyClass{
    public static void main(String[] args){
        Dog goldenRetriever = new Dog("Golden Retrieber", 60, 10);
        System.out.println(goldenRetriever.bark());
        System.out.println(goldenRetriever.calcHumanAge());

        Dog siberianHusky = new Dog("Siberian Husky", 55, 6);
        System.out.println(siberianHusky.bark());
        System.out.println(siberianHusky.calcHumanAge());

        Dog poodle = new Dog("poodle", 10, 1);
        System.out.println(poodle.bark());
        System.out.println(poodle.calcHumanAge());

        Dog shibainu = new Dog("shibainu", 35, 4);
        System.out.println(shibainu.bark());
        System.out.println(shibainu.calcHumanAge());

    }
}
