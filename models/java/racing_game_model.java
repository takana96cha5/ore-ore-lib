class Car{
    public static int wheels = 4;

    public String make;
    public String model;
    public int year;
    public String vin;
    public String color;
    public double velocity;
    public double fuelEconomy;
    public double tankCapacity;
    public double weightKg;

    public Car(String make, String model, int year, String vin, String color, double velocity, double fuelEconomy, double tankCapacity, double weightKg){

        this.make = make;
        this.model = model;
        this.year = year;
        this.vin = vin;
        this.color = color;
        this.velocity = velocity;
        this.fuelEconomy = fuelEconomy;
        this.tankCapacity = tankCapacity;
        this.weightKg = weightKg;
    }

    public String getCarString(){
        return this.make + " " + this.model + " Year: " + this.year + " Vin: " + this.vin + " Color: " + this.color + " Velocity: " + this.velocity + "mps Fuel economy: " + this.fuelEconomy + "mile/gallon Tank capacity: " + this.tankCapacity + " Weight: " + this.weightKg +"Kg. It has " + this.wheels + " wheels.";
    }

    // 停止せずに移動できる最大マイル数を計算します
    // 燃費とタンクの大きさから算出できます
    public double milesWithoutStop(){
        return this.fuelEconomy * this.tankCapacity;
    }

    // 1 時間に進むことができる距離を計算します
    public double getDistance(){
        return this.velocity * 60 * 60;
    }

    // ガソリンが空になるのにかかる時間を計算します
    public double hoursToEmpty(){
        return Math.round(this.milesWithoutStop() / this.getDistance() *100d)/100d;
    }

    // 車が持つ運動エネルギーを計算します
    // 運動エネルギー　= 1/2 mv^2
    public double getEnergy(){
        return Math.pow(this.velocity, 2) * this.weightKg / 2;
    }

}

class Main{
    public static void main(String[] args){
        Car teslaS = new Car("Tesla", "Model S", 2013, "5YJSA1CN0DFP13393", "Black", 0.04, 98 , 12, 2162);

        System.out.println(teslaS.getCarString());
        System.out.println(teslaS.milesWithoutStop());
        System.out.println(teslaS.getDistance());
        System.out.println(teslaS.hoursToEmpty());
        System.out.println(teslaS.getEnergy());

        Car porsche88 = new Car("Porsche", "928", 1988, "WP0JB0926JS861742", "Red", 0.057, 36, 12, 1390);

        System.out.println(porsche88.getCarString());
        System.out.println(porsche88.milesWithoutStop());
        System.out.println(porsche88.getDistance());
        System.out.println(porsche88.hoursToEmpty());
        System.out.println(porsche88.getEnergy());


        Car ferrari08 = new Car("Ferrari", "F430 Spyder", 2008, "ZFFEZ59E780163510", "Orange", 0.059, 11, 18, 1570);

        System.out.println(ferrari08.getCarString());
        System.out.println(ferrari08.milesWithoutStop());
        System.out.println(ferrari08.getDistance());
        System.out.println(ferrari08.hoursToEmpty());
        System.out.println(ferrari08.getEnergy());
    }
}
