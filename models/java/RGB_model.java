class RGB {
    public int red;
    public int green;
    public int blue;

    public RGB(int red, int green, int blue) {
        this.red = red;
        this.green = green;
        this.blue = blue;
    }

    public String getHexCode() {
        return "#"+String.format("%02x", Integer.valueOf(this.red)) + String.format("%02x", Integer.valueOf(this.green)) + String.format("%02x", Integer.valueOf(this.blue));
    }

    public String getBits() {
        String hex = this.getHexCode().substring(1);
        int dec = Integer.parseInt(hex, 16);
        return Integer.toBinaryString(dec);
    }

    public String getColorShade() {
        if(this.red == this.green && this.green == this.blue) return "grayscale";
        int greatest = this.red;
        String greatestString = "red";
        if(greatest < this.green){
            greatestString = "green";
            greatest = this.green;
        }
        if(greatest < this.blue){
            greatestString = "blue";
            greatest = this.blue;
        }
        return greatestString;
    }

}

class MyClass{

    public static void main(String[] args){

        RGB color1 = new RGB(0, 153, 255);
        System.out.println(color1.getHexCode()); // --> #0099ff
        System.out.println(color1.getBits());// --> 1001100111111111
        System.out.println(color1.getColorShade()); //  --> blue

        RGB color2 = new RGB(255, 153, 204);
        System.out.println(color2.getHexCode()); //  --> #ff99cc
        System.out.println(color2.getBits()); //  --> 111111111001100111001100
        System.out.println(color2.getColorShade()); //  --> red

        RGB color3 = new RGB(0, 87, 0);
        System.out.println(color3.getHexCode()); //  --> #005700
        System.out.println(color3.getBits()); //  --> 101011100000000
        System.out.println(color3.getColorShade()); //  --> green


        RGB gray = new RGB(123, 123, 123);
        System.out.println(gray.getHexCode()); //  --> #7b7b7b
        System.out.println(gray.getBits()); //  --> 11110110111101101111011
        System.out.println(gray.getColorShade()); //  --> grayscale


    }
}
