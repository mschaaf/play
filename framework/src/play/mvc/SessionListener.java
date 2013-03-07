package play.mvc;

import play.mvc.Scope.Session;

public interface SessionListener {

	public void doOnTimeout(Session oldSession);
}
