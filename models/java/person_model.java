class Person {
   // ここからクラス記述してください
      public String firstName;
      public String lastName;

      public Person(String firstName, String lastName){
         this.firstName = firstName;
         this.lastName = lastName;
      }

      public String getFullName(){
         return this.firstName + " " + this.lastName;
      }

      public String getInitial(){
         return this.firstName.charAt(0) + "." + this.lastName.charAt(0);
      }
}

class MyClass{
   public static void main(String[] args){
      Person mike = new Person("Michael", "Johnson");
      System.out.println(mike.getFullName());
      System.out.println(mike.getInitial());

      Person carly = new Person("Carly", "Angelo");
      System.out.println(carly.getFullName());
      System.out.println(carly.getInitial());

      Person jessie = new Person("Jessie", "Raelynn");
      System.out.println(jessie.getFullName());
      System.out.println(jessie.getInitial());
   }
}
