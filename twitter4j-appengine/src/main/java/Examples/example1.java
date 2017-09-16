package Examples;

import java.util.List;

import twitter4j.*;

public class example1 {
	public static void method1() throws TwitterException {
		Twitter twitter = TwitterFactory.getSingleton();
		List<Status> statuses = twitter.getHomeTimeline();
		 
	    System.out.println("Showing home timeline.");
	    for (Status status : statuses) {
	        System.out.println(status.getUser().getName() + ":" +
	                           status.getText());
	    }
	}
	public static void main(String [ ] args) throws TwitterException {
		System.out.println(1);
		method1();
	}
}
 
