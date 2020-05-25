node{
    def app
        stage('Cloning Repository') {
            checkout scm
        }
        stage('Testing Code')
        {
                sh 'python3 test.py'  
        }
        stage('Containerizing')
        {
                app = docker.build("ankitpd/project_approval_system")
        }
        stage('Pushing Image')
      {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
      }
    stage('Stopping Old Version')
    {
        def jobname = "deploy_pas"
        def buildnum = 13
        def job = Jenkins.instance.getItemByFullName(jobname)
            for (build in job.builds) {
                if (buildnum == build.getNumber().toInteger()){
                    //if (build.isBuilding()){
                        build.doStop();
                        build.doKill();
                    }
                }
            }
    }
    stage('Deploying New Version')
    {
        build job: 'deploy_pas'
    }
}
