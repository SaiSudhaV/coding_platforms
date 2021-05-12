package UberEats;

import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Customer implements Serializable{
	private String userId;
	private String password;
	
	public String getUserId() {
		return userId;
	}
	public void setUserId(String userId) {
		this.userId = userId;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}		
}

public class Login {
	Scanner scan = new Scanner(System.in);
	
	public Customer readObject1(ObjectInputStream is) {
		Customer object = null;
		try {
			object = (Customer)is.readObject();
			return object;
		}
		catch (Exception ex) {
			System.out.println(ex);
		}
		return object;
	}
	
	@SuppressWarnings("unchecked")
	public boolean signIn() {
		try {
			FileInputStream fis = new FileInputStream("Customers.txt");
			ObjectInputStream is = new ObjectInputStream(fis);
			List<Customer> list;
			
			list = (ArrayList<Customer>)is.readObject();
			int i = 1;
			
			System.out.print("Enter User ID  : ");
			String userId = scan.next();
			System.out.print("Enter Password : ");		
			String password = scan.next();
			
			for(Customer customer : list) {
				if(customer.getUserId().equals(userId) && customer.getPassword().equals(password)) {
					return true;
				}
			}
			
			is.close();
			fis.close();
		}
		catch (Exception ex) {
			System.out.println(ex);
		}
		
		return false;
	}
	
	@SuppressWarnings("unchecked")
	public void register() {	
		List<Customer> list = new ArrayList<Customer>();
		
		Customer customer = new Customer();
		System.out.print("Enter User ID  : ");
		customer.setUserId(scan.next());
		System.out.print("Enter Password : ");		
		customer.setPassword(scan.next());
		
		FileInputStream fis;
		ObjectInputStream is;
		FileOutputStream fos;
		ObjectOutputStream os;
		
		try {			
			fis = new FileInputStream("Customers.txt");
			is = new ObjectInputStream(fis);			
			list = (ArrayList<Customer>)is.readObject();	
			is.close();
			fis.close();
		}
		catch (Exception e) { 
			
		}
		
		try {
			fos = new FileOutputStream("Customers.txt");
			os = new ObjectOutputStream(fos);
			
			list.add(customer);
			os.writeObject(list);
			os.close();
			fos.close();
		}
		catch (Exception ex) {			
		}
		
		System.out.println("Customer Registered Successfully!!! \n");
	}
	
	public void mainMenu() {
		Login login = new Login();
		int choice = 0;
				
		System.out.println("Select Your Choice");
		System.out.println("==================");
			
		System.out.println("1. Login");
		System.out.println("2. Register");
		System.out.println("3. Exit \n");
			
		System.out.print("Enter Your Choice : ");
		choice = scan.nextInt();
		System.out.println();
			
		if(choice == 1) {
			if(login.signIn()) {
				System.out.println("Successfully SignIn \n");
				
				
				
			}
			else {
				System.out.println("Login Failed!!!\n");
				mainMenu();
			}
		}
		else if(choice == 2) {
			login.register();	
			mainMenu();
		}	
		else if(choice == 3) {
			System.out.println("Application Terminated!!! \n");
		}
		else {
			mainMenu();
		}
	}
    public static void main(String[] args) {
    	Restaurant[] restaurant = new Restaurant[200];
		restaurant[0] = new Restaurant(1, "Mehfil", "Indian");
		restaurant[1] = new Restaurant(1, "Pista House", "Chinese");
		restaurant[2] = new Restaurant(1, "Sweet Magic", "Continental");
		restaurant[3] = new Restaurant(1, "Rang", "Indian");
		restaurant[4] = new Restaurant(1, "Behrouz Biriyani", "Arabian");
		restaurant[5] = new Restaurant(1, "Dominos", "Continental");
				
		restaurant[6] = new Restaurant(2, "The Shawarma Company", "Arabian");
		restaurant[7] = new Restaurant(2, "Pizza Hut", "American");
		restaurant[8] = new Restaurant(2, "Burger King", "Continental");
		restaurant[9] = new Restaurant(2, "Bahar Cafe", "Indian");
		restaurant[10] = new Restaurant(2, "Republic of Noodles", "Chinese");
			
		restaurant[11] = new Restaurant(3, "Kritunga", "Indian");
		restaurant[12] = new Restaurant(3, "Swagath", "Chinese");
		restaurant[13] = new Restaurant(3, "Lemon Tree","Arabian" );
		restaurant[14] = new Restaurant(3, "KFC", "American");
		restaurant[15] = new Restaurant(3, "RedFox", "Continental");
		   
		restaurant[16] = new Restaurant(4, "Sitara Grand", "Indian");
		restaurant[17] = new Restaurant(4, "Siesta", "Chinese");
		restaurant[18] = new Restaurant(4, "McDonalds", "American");
		restaurant[19] = new Restaurant(4, "Makers of Milk Shakes", "Continental");
		restaurant[20] = new Restaurant(4, "Cream Stone","American");
		      
		Menu[] item = new Menu[100];
		item[0] = new Menu("Chicken Boneless Biriyani", 400, "Indian");
		item[1] = new Menu("Gongura Mutton Biryani", 500, "Indian");
		item[2] = new Menu("Parata with Paneer Butter Masala", 300, "Indian");
		item[3] = new Menu("Natu Kodi Biryani", 350, "Indian");
		item[4] = new Menu("Dosa with Mutton", 400, "Indian");
		item[5] = new Menu("Egg Fried Rice", 300, "Chinese");
		item[6] = new Menu("Veg Fried Rice", 400, "Chinese");
		item[7] = new Menu("Shrimp Noodles", 400, "Chinese");
		item[8] = new Menu("Veg Noodles with Manchurian", 400, "Chinese");
		item[9] = new Menu("Chicken Noodles", 400, "Chinese");
			
		item[10] = new Menu("Crispy Chicken Burger", 80, "American");
		item[11] = new Menu("Chicken Keema Burger", 100, "American");
		item[12] = new Menu("Chicken Whooper Burger", 120, "American");
		item[13] = new Menu("Tropical Coconut Icecream", 200, "American");
		item[14] = new Menu("Oreo Nutella Milkshake", 180, "American");
		
		item[15] = new Menu("Subz - E - Biriyani", 300, "Arabian");
		item[16] = new Menu("Murgh Makhani Biriyani", 350, "Arabian");
		item[17] = new Menu("Murgh Kefta", 210, "Arabian");
		item[18] = new Menu("Falafel-E-khaas", 290, "Arabian");
		item[19] = new Menu("Murgh Koobideh", 150, "Arabian");
				
		item[20] = new Menu("The Farmer's Omlette", 299, "Continental");
		item[21] = new Menu("Cheese Burger", 190, "Continental");
		item[22] = new Menu("Killer Egg", 160, "Continental");
		item[23] = new Menu("Fried Chicken Sandwich",200, "Continental");
		item[24] = new Menu("Paneer Club Sandwich", 100, "Continental");
		item[25] = new Menu("Cheese Garlic Bread", 150, "Continental");
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter your nearest location :\n1)KUKATPALLY\n2)HITECH CITY\n3)AMERPEET\n4)MIYAPUR");
		int userlocation = scan.nextInt();
		
		
		for(;;) {
			
			System.out.println("Available Restaurants by ID : ");
			for(int i = 0; i < 21; i++) {
				if(userlocation == restaurant[i].getLocationID()) {
					System.out.println(restaurant[i].getName());
					System.out.println("Cuisine:" + restaurant[i].getCuisine() +"  ID-"+restaurant[i].getRestaurantID());
					System.out.println("\n");
				}
			}
			System.out.println("Choose a Restaurant and type it's Cuisine: ");
			
			String food = scan.next();
			for(int j = 0; j < 25; j++) {
				if(food.equals(item[j].getCuisine())) {
					System.out.println("ID-" + item[j].getItemID()+" "+item[j].getItemName() + " - Rs." +item[j].getPrice() + "/-");
				}
			}
			System.out.println("Add food to your cart :");
			
			Login obj = new Login();
			obj.mainMenu();	
			int choice;
			for(;;) {
				int [] arr = new int[6];
				for(int j = 0; j < 25; j++) {
					if(food.equals(item[j].getCuisine())) {
						System.out.println("ID-" + item[j].getItemID()+" "+item[j].getItemName() + " - Rs." +item[j].getPrice() + "/-");
					}
				}
				
				int bill = 0;
				System.out.println("Number of items you want to order :");
				int n = scan.nextInt();
				
				System.out.println("Enter ID for adding ");
				for(int i = 0; i < n; i++) {
					arr[i] = scan.nextInt();
					bill = bill + item[arr[i]].getPrice();
					if(arr[i] == 99) {
						break;
					}
				}
				
				System.out.println("View your cart : ");
				for(int k = 0; k < n; k++ ) {
					System.out.println(item[arr[k]].getItemName() + " -  Rs." +item[arr[k]].getPrice() +"/-" );
				}
						
				System.out.println("Total bill " + bill);
				System.out.println("Your order is confirmed!!!");
				System.out.println("press 1 for logout and 2 to order again\n");
				choice = scan.nextInt();
				if(choice == 1) {
					break;
				}
						
			}
			int exitChoice;
			System.out.println("press 1 to exit and 2 for choosing next restaurant");
			exitChoice = scan.nextInt();
			if(exitChoice == 1) {
				break;
			}
			System.out.println("Enter your nearest location :\n1)KUKATPALLY\n2)HITECH CITY\n3)AMERPEET\n4)MIYAPUR");
			userlocation = scan.nextInt();
					
			
		}

		
			

    	
    }
        	        
	
}
	
	
		
		
		
		
		
		


	






