class Car{
    // Car クラスのメンバ変数の宣言
    // 変更すべきではないものを private に設定している点に注意してください。このスコープのみが読み込んだり変更したりすることができます
    // どのスコープでも変更できるのは color だけです
    private String make;
    private String model;
    private String vin;
    public String color;

    // コンストラクタ
    public Car(String make, String model, String vin, String color){
        this.make = make;
        this.model = model;
        this.vin = vin;
        this.color = color;
    }

    public String getCarString(){
        // この関数は Car クラスのスコープ内にあるので、private 変数の全てにアクセスすることができます
        return this.make + " " + this.model + " " + this.vin + " " + this.color;
    }

    // private の各変数にアクセスする方法がないので、ゲッターメソッドを作成して、状態から各データを読み取ります
    public String getMake(){
        // make の中に格納されている値のコピーを返します
        return this.make;
    }

    public String getModel(){
        return this.model;
    }

    public String getVin(){
        return this.vin;
    }

    // オブジェクトの状態の変更。現在の model を入力値に変更します
    public void setModel(String newModelValue){
        this.model = newModelValue;
    }
}

class Main{
    public static void main(String[] args){
        Car teslaS = new Car("Tesla", "Model S", "5YJSA1CN0DFP13393", "Black");
        System.out.println(teslaS.getCarString());

        // public に設定してある color にアクセスし編集するのは可能です
        System.out.println(teslaS.color);
        teslaS.color = "Green";
        System.out.println("teslaS new state is: " + teslaS.getCarString());

        // ゲッターメソッド
        System.out.println("Printing and changing teslaS model..." + teslaS.getModel());

        // 名前を Model Y に変更します
        teslaS.setModel("Model Y");
        System.out.println("teslaS new state is: " + teslaS.getCarString());

        // 車の vin number を変更することはできません。したがって次の処理はエラーを起こします
        // teslaS.vin = "WB10228019ZT94950";
    }
}
