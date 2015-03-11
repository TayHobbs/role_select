(ns role-select.core
  (:gen-class))

(def Warrior
  {:name "Brothgar" :role "Warrior" :weapon "Shield"})

(def Priest
  {:name "Alinia" :role "Priest" :weapon "Staff"})

(def Rouge
  {:name "Granzine" :role "Rouge" :weapon "Daggers"})

(def questions
    ["Do you like protecting your friends? (y/n) => "
    "Do you like being a leader? (y/n) => "
    "Do you like being in the background? (y/n) => "
    "Do you like dealing damage up close? (y/n) => "
    "Far away? (y/n) => "
    "Do you like working alone? (y/n) => "
    "Do you like melee? (y/n) => "
    "Ranged? (y/n) => "])

(defn print-questions [questions]
  (reduce (fn [answer question]
    (println question)
    (if (= "y" (read-line))
      (inc answer)
          answer))
          0
          questions))

(defn suggest-role [number]
  (if (<= number 3)
    (let [role "Priest"]
       role)
    (if (<= number 5)
      (let [role "Rouge"]
         role)
      (let [role "Warrior"]
         role))))

(defn set-role [role]
  (println (str "Your suggested role is a " role ". Are you happy with this choice? (y/n) => "))
  (if (= "y" (read-line))
    role
  (println "Suggest New Role")))

(defn -main [& args]
  (let [number (print-questions questions)]
    (let [role (suggest-role number)]
      (set-role role))))
