import java.util.Calendar;

class Person{
    public String firstName;
    public String lastName;
    public double heightM;
    public double weightKg;
    public int birthYear;

    public Person(String firstName, String lastName, double heightM, double weightKg, int birthYear){
        this.firstName = firstName;
        this.lastName = lastName;
        this.heightM = heightM;
        this.weightKg = weightKg;
        this.birthYear = birthYear;
    }

    public String getStateString(){
        return "First Name: " + this.firstName + ", Last Name: " + this.lastName + ", heightM: " + this.heightM + ", weightKg: " + this.weightKg + ", birthYear: " + this.birthYear;
    }

    public String getFullName(){
        return this.firstName + " " + this.lastName;
    }

    public int getAge(){
        int currentYear = Calendar.getInstance().get(Calendar.YEAR);
        return currentYear - this.birthYear;
    }

    public double getBmi(){
        return this.weightKg / (Math.pow(this.heightM,2));
    }

    public double eat(double calories){
        this.weightKg += calories/7700;
        return this.weightKg;
    }

    // 運動を文字列として受け取り、1 分間に消費されたカロリー数を返します
    public double caloriesBurnedPerMinuteExercise(String exercise){
        // 燃焼カロリーは MET(Metabnolic Equivalent of Task) を使って計算することができます
        double met = 1;
        if(exercise == "running") met = 8;
        else if(exercise == "walking") met = 3;
        else if(exercise == "tennis") met = 5;
        else if(exercise == "rope jump") met = 9;

        // 燃焼カロリーは、met * 3.5 * weight / 200 によって計算することができます
        return met * 3.5 * this.weightKg / 200;
    }

    // 運動を文字列として受け取り、1 kg痩せるのに何時間かかるかを返します
    public double hoursToLose1KgByExercise(String exercise){
        return 7700 / (this.caloriesBurnedPerMinuteExercise(exercise) * 60);
    }

    // 運動、時間を入力として受け取り、燃焼されたカロリー数を計算し、体重を更新して新しい体重を返します
    public double exercise(String exercise, int minutes){
        // 関数の分解
        double caloriesBurned = this.caloriesBurnedPerMinuteExercise(exercise) * minutes;
        this.weightKg -= caloriesBurned/7700;
        return this.weightKg;
    }
}

class Main{
    public static void main(String[] args){
        Person carly = new Person("Carly", "Angelo", 1.72, 85.5, 1996);
        System.out.println(carly.getStateString());

        System.out.println("Carly burns: " + carly.caloriesBurnedPerMinuteExercise("running") + " calories per minute running");
        System.out.println("It takes carly: " + carly.hoursToLose1KgByExercise("running") + " hours running to burn 1 kg");

        carly.exercise("running", 600);
        System.out.println("Carly went running for 10 hours.");
        System.out.println(carly.getStateString());
    }
}
